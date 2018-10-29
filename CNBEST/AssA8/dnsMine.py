import os
import socket

def host_to_addr():
	try:
		print('Host address: ',socket.gethostbyname(input('Enter host name:\n ')))
	except Exception as e:
		print(e)
def addr_to_host():
	try:
		print('Host name: ',socket.gethostbyaddr(input('Enter host address:\n ')))
	except Exception as e:
		print(e)			

def nslookup():




import os
import socket

def host_to_addr():
	try:
		print('Host address:',socket.gethostbyname(input('Enter host name:\n>')))
	except Exception as e:
			print(e)
def addr_to_host():
	try:
		print('Host name:',socket.gethostbyaddr(input('Enter host address:\n>')))
	except Exception as e:
		print(e)
def nslookup():
	try:
		string=input('Enter URL or IP address:')
		os.system('nslookup ' + string)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	
	while True:
		choice=input('\n\nEnter choice\n1.Get host name\n2.Get host address\n3.Nslookup\n4.Exit\n>')
		if choice == '1':
			host_to_addr()
		elif choice == '2':
			addr_to_host()
		elif choice == '3':
			nslookup()
		else:
			break




















































































































































































































