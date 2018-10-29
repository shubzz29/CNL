import sys
import threading
import socket

global message
class Server():
	def __init__(self,port):
		self.ip='127.0.0.1'
		self.port=port
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.bind((self.ip,self.port))
		self.client1=None
		self.client2=None
		self.clients={}
		
	def get_clients(self):
		self.name1, self.address1 = self.sock.recvfrom(4096)
		self.name2, self.address2 = self.sock.recvfrom(4096)
		self.clients[str(self.address2[0])+str(self.address2[1])]=self.name2
		self.clients[str(self.address1[0])+str(self.address1[1])]=self.name1
		print('Address1 {} : {} \n Address2 {} : {} '.format(self.address1,self.name1.decode(encoding='UTF-8'),self.address2,self.name2.decode(encoding='UTF-8')))
		print('Starting ChatRoom for {} and {}'.format(self.name1.decode(encoding='UTF-8'),self.name2.decode(encoding='UTF-8')))
		
	def first_client(self):
		print('First Sender')
		global message
		while True:
			message, address = self.sock.recvfrom(4096)
			
			if message.decode(encoding='UTF-8')!='bye':
				print('{}:{}'.format(self.clients[str(address[0])+str(address[1])].decode(encoding='UTF-8'),message.decode(encoding='UTF-8')))

				if address == self.address1:
					self.sock.sendto(message, self.address2)
				elif address == self.address2:
					self.sock.sendto(message, self.address1)
			else:
				print('Chat Room over')
				break			
	def second_client(self):
		print('Second Sender')
		global message
		while True:
			message, address = self.sock.recvfrom(4096)
			if message.decode(encoding='UTF-8')!='bye':
				print('{}:{}'.format(self.clients[str(address[0])+str(address[1])].decode(encoding='UTF-8'),message.decode(encoding='UTF-8')))

				if address == self.address1:
					self.sock.sendto(message, self.address2)
				elif address == self.address2:
					self.sock.sendto(message, self.address1)
			else:
				print('Chat Room over')
				break
	def run(self):
		
		self.thread1 = threading.Thread(target=self.first_client, args=())
		self.thread2 = threading.Thread(target=self.second_client, args=())

		self.thread1.start()
		self.thread2.start()
		
		
		#self.thread1.join()
		#self.thread2.join()


def main():
	chatroom1=Server(5000)
	chatroom1.get_clients()
	main_thread=threading.Thread(target=chatroom1.run,args=())
	main_thread.start()
	#chatroom1.sock.close()
	
if __name__=='__main__':
	print('Server Side')
	main()


	
