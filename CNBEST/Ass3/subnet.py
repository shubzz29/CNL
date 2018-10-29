
ip = raw_input("Enter ip address >>").split(".")
if int(ip[0]) < 127:
    classtype = "Class A"
    subnet = "255.0.0.0"
    cidr = 8
elif int(ip[0]) < 192 and int(ip[0]) > 127:
    classtype = "Class B"
    subnet = "255.255.0.0"
    cidr = 16a
elif int(ip[0]) < 224:
    classtype = "Class C"
    subnet = "255.255.255.0"
    cidr = 24

value = int(raw_input("Enter CIDR >>"))
borrowedbits = value - cidr
noofnetworks = 2**borrowedbits
noofips = 2**(32-value)
noofhosts = 2**(32-value)-2
print("Borrowed Bits "+str(borrowedbits))
print(classtype+" Address, Default Subnet "+subnet)
print("You can create "+str(noofnetworks)+" networks")
print("There will be "+str(noofips)+" IP addresses on each network")
print("You will have "+str(noofhosts)+" HOST IP addresses on each network")

startwith = 0
num=0
if(classtype is "Class C"):
    for i in range(2**borrowedbits):
        print("subnet no."+str(num)+" "+ip[0]+"."+ip[1]+"."+ip[2]+"."+str(startwith)+"  -  "+ip[0]+"."+ip[1]+"."+ip[2]+"."+str(startwith+noofips-1))
        startwith += noofips
	    num+=1
