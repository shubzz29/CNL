#install sshpass package
import os;
connect="sshpass -p 'printer' ssh root@10.10.15.16"
command_install=" yum -y install nasm "
command_remove=" dnf -y remove nasm "
os.system(connect+command_install)
#print("***************************REMOVING NASM*********************************")
#os.system(connect+command_remove)

#& dnf -y remove nasm
