from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.bind(("127.0.0.1",5252))


data = s.recv(1024)
print "Received File:",data
f = open(data,'wb')
data = s.recv(1024)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data = s.recv(1024)
except timeout:
    f.close()
    s.close()
    print("File Downloaded")