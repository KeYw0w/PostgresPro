import getpass
import paramiko
import time
ip=input('Enter IP-adress')
passw = getpass.getpass(prompt="Введите пароль:")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect (ip, username='root', password=passw)
channel = ssh.get_transport().open_session()
channel.get_pty()
channel.settimeout(5)
channel.exec_command('''sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
                     ''')
# channel.exec_command("ls")
# channel.recv_exit_status()
# print(channel.recv(1024))
time.sleep(10)

channel.exec_command('''wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
''')
# channel.send(passw+'\n')
channel.recv_exit_status()
print(channel.recv(1024))
channel.close()
ssh.close()