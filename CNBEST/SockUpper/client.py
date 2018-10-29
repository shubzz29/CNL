from socket import *
ip = "127.0.0.1"
port = 5555
s = socket(AF_INET, SOCK_STREAM)
s.connect((ip,port))

msg = raw_input("Enter your line >> ")
s.send(msg)
response = s.recv(1024)
s.close()
print(response)