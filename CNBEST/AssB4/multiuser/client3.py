from socket import *
s = socket(AF_INET, SOCK_DGRAM)

serverip = "127.0.0.1"
serverport = 1337
serveraddr = (serverip,serverport)
name = "Neymar: "
print("Enter your message q for quit")
while(True):
	msg = raw_input(">>>")
	if(msg is "q"):
		s.close()
		break
	msg = name+msg
	s.sendto(msg,serveraddr)