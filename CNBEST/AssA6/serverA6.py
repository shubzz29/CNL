from socket import *

s = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 6666
s.bind((ip,port))
s.listen(4)
c, addr = s.accept()
data=c.recv(1024)
c.send("Your answer is "+str(eval(data))
s.close()
