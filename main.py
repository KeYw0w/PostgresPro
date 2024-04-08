import sh
import re
print("Enter IP-address or hostname of your server")
# ip = input()
ip="root@192.168.0.106"
try:
    connection=sh.ssh.bake(ip)
    distrib=(connection("lsb_release -a | grep Distributor"))
    Distribution=distrib.split(":")
    print(connection('''sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' '''))
    print(connection('''wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -'''))
    print(connection("apt-get update"))
    print(connection("apt-get -y install postgresql "))
    # (connection('''
    #                 sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    #                               '''))
    #sudo apt-get -y install postgresql 
    # wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
                    # sudo apt-get update
    
    
    
    
    
except:
    print("Failed to connect")
    
