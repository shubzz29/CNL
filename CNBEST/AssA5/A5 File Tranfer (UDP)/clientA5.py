from socket import *

s = socket(AF_INET,SOCK_DGRAM) 
s.connect(("127.0.0.1",5252))
file_name= "test.txt"
s.send(file_name)
f=open(file_name,"rb")
data = f.read(1024)
print("Sending ...")
while (data):
    s.send(data)
    data = f.read(1024)
s.close()
f.close()
