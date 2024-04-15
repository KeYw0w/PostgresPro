import os
import time
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


def connection(ip, username, password=None, public_key=None):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if password != None:
        cl.connect(hostname="217.25.94.30", username="root", password=pw)
    elif public_key != None:
        cl.connect(hostname="217.25.94.30", username="root", key_filename=public_key)
    return cl


def command(ssh_connection, command):
    stdin, stdout, stderr = ssh_connection.exec_command(command)
    if stdout.channel.recv_exit_status() == 0:
        return stdout.read().decode('utf-8')
    else:
        raise Exception(stdout.read().decode('utf-8'))


def check_package_manager(ssh_connection):
    return (ssh_connection, check_package)


def install_psql(ssh_connection, package_name):
    if package_name == 'yum':
        command = 'yum install -y psql'
    elif package_name == 'apt':
        command = 'apt install -y psql'
    elif package_name == 'dnf':
        command = 'dnf install -y psql'
    stdin, stdout, stderr = ssh_connection.exec_command(command)
    while stdout.readline():
        print(stdout.readline())
    print("PSQL insertion complete")


def edit_config(ssh_connection):
    path_to_conf = command(ssh_connection, "sudo -u postgres psql -c 'SHOW config_file'")
    path_to_hba = command(ssh_connection, "sudo -u postgres psql -c 'SHOW hba_file'")
    commands = [
        f'''sed -i 's/#listen_addresses = 'localhost'/listen_addresses = '*'/' {path_to_conf}''',
        f'''sed -i '/^*local connections*/a\host all all 0.0.0.0/0 md5' {path_to_hba} ''',
        '''sudo systemctl restart postgresql''']


def health_check(ssh_client):
    command = 'sudo -u postgres psql -c "SELECT (1);"'
    output = command(ssh_client, command)
    print(output)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='IP адрес или имя хоста удаленного сервера')
    return parser.parse_args()


def full_install_psql(ssh_connection):
    package_manager = check_package_manager(ssh_connection)
    install_psql(ssh_connection, package_manager)
    edit_config(ssh_connection)
    print("PSQL installing and configuring complete")


commands = {
    '1': full_install_psql,
    '2': health_check}
def print_commands():
    for command in commands:
        print(f"{command} - {commands[command].__name__}")

def main():
    USER = os.getlogin()
    PUBLICKEY = os.path.expanduser('~/.ssh/id_rsa.pub')
    arguments = parse_arguments()
    try:
        ssh_connection = connection(arguments.host, username=USER, public_key=PUBLICKEY)
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed")
        choice = input('You want to authenticate with password (1) or custom public key(2)?')
        if choice == '1':
            pw = getpass.getpass(f"Enter {USER} Password on remote host:\n")
            ssh_connection = connection(arguments.host, username=USER, password=pw)
        elif choice == '2':
            public_key = input("Enter Path to Public Key:\n")
            ssh_connection = connection(arguments.host, username=USER, public_key=public_key)

    while True:
        print_commands()
        input_user = input('Enter your choice: ')
        if input_user == 'Exit':
            print("Exiting program")
            if ssh_connection:
                ssh_connection.close()
        elif input_user in commands:
            try:
                commands[input_user](ssh_connection)
            except Exception as e:
                print("Something went wrong")
        else:
            print("Invalid command!")
if __name__ == '__main__':
    main();