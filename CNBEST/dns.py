import socket
host = raw_input("Enter host by name : ")
addr1 = socket.gethostbyname(host)
print(addr1)


ip = raw_input("Enter host by IP : ")
addr2 = socket.gethostbyaddr(ip)
print(addr2)
