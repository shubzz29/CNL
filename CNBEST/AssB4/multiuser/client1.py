from socket import *
s = socket(AF_INET, SOCK_DGRAM)

ip = "127.0.0.1"
port = 1337
addr = (serverip,serverport)
name = "Messi: "
print("Enter your message q for quit")
while(True):
	msg = raw_input(">>>")
	if(msg is "q"):
		s.close()
		break
	msg = name+msg
	s.sendto(msg,addr)
