from socket import *
ip = "127.0.0.1"
port = 5555
s = socket(AF_INET, SOCK_STREAM)
s.bind((ip,port))

s.listen(4)
c, addr = s.accept()
data = c.recv(1024)
print("Received Data : >> ",data)
c.send(data.upper())
print(data.upper())
s.close()