from socket import *
import time

s = socket(AF_INET, SOCK_DGRAM)
ip = "127.0.0.1"
port = 1337
s.bind((ip,port))
now = int(time.time())
while(True):
	if(int(time.time())-now > 600):
		s.close()
		break
		#s.close()
	message = s.recv(1024)
	print(message)
	

