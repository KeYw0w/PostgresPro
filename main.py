import os
import getpass
import paramiko
import argparse

check_package = '''
                if which apt-get >/dev/null 2>&1; then 
                         echo apt;
                elif which dnf>/dev/null 2>&1; then  
                   echo dnf;
                elif which yum >/dev/null 2>&1; then 
                    echo yum; 
                elif which dnf > /dev/null 2>&1; then 
                     echo dnf;
                    fi'''


def connection(ip, username=None, password=None, key=None, port=None):
    try:
        if port is None:
            port=22
        cl = paramiko.SSHClient()
        cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if password is None:
            cl.connect(hostname=ip, username=username, password=password, port=port)
        else:
            cl.connect(hostname=ip, username=username, pkey=key)
    except Exception as e:
        print(e)
    return cl


def ssh_command(ssh_connection, command):
    stdin, stdout, stderr = ssh_connection.exec_command(command)
    if stdout.channel.recv_exit_status() == 0:
        return stdout.read().decode('utf-8')
    else:
        print(stdout.read().decode('utf-8'))
        # print(stdin.read().decode('utf-8'))
        raise Exception(stderr.read().decode('utf-8'))


def check_package_manager(ssh_connection):
    return (ssh_command(ssh_connection, check_package))


def install_psql(ssh_connection, package_name):
    if package_name == "yum\n":
        command = "yum install -y postgresql-16"
    elif package_name == "apt\n":
        command = "sudo apt update && sudo apt install -y postgresql-16"
    elif package_name == "dnf\n":
        command = "dnf install -y postgresql-16"
    stdin, stdout, stderr = ssh_connection.exec_command(command=command)
    while line := stdout.readline(): print(line)
    print("PSQL insertion complete")


def edit_config(ssh_connection):
    start_psql = ssh_command(ssh_connection, "service postgresql start")
    print(ssh_command(ssh_connection, "whoami"))
    path_to_conf = ssh_command(ssh_connection, "sudo -u postgres psql -c 'SHOW config_file' | grep 'postgresql'")
    path_to_hba = ssh_command(ssh_connection, "sudo -u postgres psql -c 'SHOW hba_file' | grep 'pg_hba'")
    commands = [
        f'''echo -e "listen_addresses = '*'" >> {path_to_conf}''',
        f'''sudo echo -e "host\tall\tall\t0.0.0.0/0\tpassword" >> {path_to_hba}''',
        "sudo service postgresql restart",
        f'''sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres'"'''
    ]
    for command in commands:
        ssh_command(ssh_connection, command)
        print(command)


def health_check(ssh_connection):
    command = f'''sudo -u postgres psql -c "SELECT 1;"'''
    output = ssh_command(ssh_connection, command)
    print(output)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='IP адрес или имя хоста удаленного сервера')
    parser.add_argument('--port', help="port по которому работает ssh")
    return parser.parse_args()


def full_install_psql(ssh_connection):
    package_manager = check_package_manager(ssh_connection)
    print(1)
    install_psql(ssh_connection, package_manager)
    print(2)
    edit_config(ssh_connection)
    print("PSQL installing and configuring complete")


commands = {
    '1': full_install_psql,
    '2': health_check,
}


def print_commands():
    for command in commands:
        print(f"{command} - {commands[command].__name__}")


def main():
    USER = os.getlogin()
    PUBLICKEY = os.path.expanduser('~/.ssh/id_rsa.pub')
    print(PUBLICKEY)
    arguments = parse_arguments()
    try:
        ssh_connection = connection(arguments.host, username="root", key=PUBLICKEY, port=arguments.port)
        print( arguments.port)
    except Exception as e:
        choice = input('You want to authenticate with password (1) or custom public key(2)?')
        if choice == '1':
            pw = getpass.getpass(f"Enter {USER} Password on remote host:\n")
            ssh_connection = connection(ip=arguments.host, username="keyw0w", password=pw)
        elif choice == '2':
            public_key = input("Enter Path to Public Key:\n")
            ssh_connection = connection(ip=arguments.host, username=USER, public_key=public_key)
    while True:
        print_commands()
        input_user = input('Enter your choice: ')
        if input_user.lower() == 'exit':
            print("Exiting program")
            if ssh_connection:
                ssh_connection.close()
            exit(0)
        elif input_user in commands:
            try:
                commands[input_user](ssh_connection)
            except Exception as e:
                print("Something went wrong")
        else:
            print("Invalid command!")


if __name__ == '__main__':
    main()
