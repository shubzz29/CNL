from socket import *

s = socket(AF_INET,SOCK_DGRAM) 
addr=("127.0.0.1",5252)
file_name= "test.txt"
s.sendto(file_name,addr)
f=open(file_name,"rb")
data = f.read(1024)
print("Sending ...")
while (data):
    s.sendto(data,addr)
    data = f.read(1024)
s.close()
f.close()
