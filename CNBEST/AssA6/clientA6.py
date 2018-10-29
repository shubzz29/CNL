from socket import *

s = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 6666
s.connect((ip,port))
expr = input("Enter arithmetic expression e.g 3+5 ")
s.send(str(expr))
data = s.recv(1024)
print(str(data))
s.close()