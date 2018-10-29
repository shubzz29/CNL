import ipaddress
import math
import os
import subprocess

#default subnetmask
subnet_mask={'A':'255.0.0.0','B':'255.255.0.0','C':'255.255.255.0','D':'255.255.255.255'}

#identifies class of ip addr(classful)

def findClass(ip_addr,n):
	octet=ip_addr.split('.')
	new_mask=""
	net_id=""
	if int(octet[0]) in range(0,128) and n<=24:
		print('Class A')
		print("Old Subnet=="+subnet_mask['A'])
		l1=subnet_mask['A'].split('.')
		temp=0
		for i in range(0,n):	
        		temp=temp+2**(7-i)
			
		
		l1[1]=str(temp)
		new_mask=".".join(l1)
		print("New subnet=="+ new_mask)
		net_id=octet[0]+'.0.0.0'
	

	elif int(octet[0]) in range(128,192) and n<=16:
		print('Class B')
		print("Old Subnet=="+subnet_mask['B'])
		l1=subnet_mask['B'].split('.')
		temp=0
		for i in range(0,n):	
        		temp=temp+2**(7-i)
			
		
		l1[2]=str(temp)
		new_mask=".".join(l1)
		print("New subnet=="+new_mask)
		net_id=octet[0]+"."+octet[1]+'.0.0'	
		
	elif int(octet[0]) in range(192,224) and n<=8:
		print('Class C')
		print("Old Subnet=="+subnet_mask['C'])
		l1=subnet_mask['C'].split('.')

		temp=0
		for i in range(0,n):	
        		temp=temp+2**(7-i)
			
		
		l1[3]=str(temp)
		new_mask=".".join(l1)
		print("New subnet=="+new_mask)
		net_id=octet[0]+"."+octet[1]+"."+octet[2]+'.0'
	return new_mask,net_id	
	
	
def subnet_mask_classless(length):
	mask=[]
	if length <8 :
		
		temp=0
		for i in range(0,length):	
			temp=temp+2**(7-i)
			mask.append(str(temp))
			mask.append('0')
			mask.append('0')
			mask.append('0')
		
	if length>=8 and length<16:
		mask.append('255')
		if(length>8):
			length-=8
			temp=0
			for i in range(0,length):	
				temp=temp+2**(7-i)
			
			mask.append(str(temp))
			mask.append('0')
			mask.append('0')
		else:
			mask.append('0')
			mask.append('0')
			mask.append('0')
			
		
			
	elif length>=16 and length<24:
		mask.append('255')
		mask.append('255')
		if(length>16):
			length-=16
			temp=0
			for i in range(0,length):	
				temp=temp+2**(7-i)
			mask.append(str(temp))
			mask.append('0')
		else:
			mask.append('0')
			mask.append('0')

	elif length>=24 and length<32:
		mask.append('255')
		mask.append('255')
		mask.append('255')
		if(length>24):
			length-=24
			temp=0
			for i in range(0,length):	
				temp=temp+2**(7-i)
			mask.append(str(temp))
        	
	return ".".join(mask)
		

		
	
	

	
#creates subnets	

def subNet(ip_addr,subnets_gr,no_of_subnets):
	for i, subnet in enumerate(subnets_gr):
		if(i<no_of_subnets):
        		print('\nSubnet %s'%(i))
        		print('First address = %s'%(subnet[0]))
        		print('Last address = %s'%(subnet[-1]))

#to ping machine of same subnet

def ping(ip_addr,subnets_gr):
	alt_ip=input("Enter ip to ping==")
	print("\n *************PING**************")
	num=0
	for sub in subnets_gr:
		if ipaddress.IPv4Address(alt_ip) in sub:
			print('The machine ip you want to ping is in %s subnet'%(num))
			break
		num += 1
	num2=0
	for sub in subnets_gr:
		if ipaddress.IPv4Address(ip_addr) in sub:
			print('Your ip is in %s subnet'%(num2))
			break
		num2 += 1
	out=0
	try:
		if not ipaddress.IPv4Address(alt_ip) in subnets_gr[num]:
			print('IP address is not valid in given subnet')
		elif num!=num2:
			print("Not possible to ping as not in same subnet")
		elif ipaddress.IPv4Address(alt_ip) in subnets_gr[num] and ipaddress.IPv4Address(alt_ip)==subnets_gr[num][0]:
			print("Cannot ping subnet id")
		elif ipaddress.IPv4Address(alt_ip) in subnets_gr[num] and ipaddress.IPv4Address(alt_ip)==subnets_gr[num][-1]:
			print("Cannot ping broadcast")
		else:
			print("IP can be pinged!")
			proc = subprocess.Popen(['ping', '-c', '3', alt_ip],stdout=subprocess.PIPE)
			#os.system("ping "+alt_ip+" -c 3")
			stdout, stderr = proc.communicate()
			if proc.returncode == 0:
				print('Machine with ip %s is UP'%(alt_ip))
				#print('ping output:')
				#print(stdout.decode('ASCII'))
			else:
				print('Machine with ip %s is DOWN'%(alt_ip))

	except Exception:
		print("IP address not in given subnet list!!")
	
		
#change ip
	
def changeip(new_ip,netmask):
	list_of_interfaces=os.listdir('/sys/class/net/')
	print("********INTERFACES AVAILABLE************")
	for i,j in enumerate(list_of_interfaces):
		print(" %s"%(i+1)+ ". " + j)
	mno=int(input("Select interface=="))
	print("Old IP:")
	mno-=1
	x=os.system('ip -4 addr show '+list_of_interfaces[mno] +' | grep -oP "(?<=inet\s)\d+(\.\d+){3}"')
	
	#new_ip=input("Enter new ip==")
	os.system('sudo ifconfig %s '%(list_of_interfaces[mno])+' down')
	os.system('sudo ifconfig %s '%(list_of_interfaces[mno])+new_ip+" netmask "+netmask)
	os.system('sudo ifconfig %s '%(list_of_interfaces[mno])+' up')
	print("New IP:")
	x=os.system('ip -4 addr show ens33 | grep -oP "(?<=inet\s)\d+(\.\d+){3}"')

def find_net_id_classless(ip_addr,mask):
	ipaddr=ip_addr.split('.')
	#print(ipaddr)
	sub_mask=mask.split('.')
	#print(sub_mask)
	res=[]
	for i in range(4):
		res.append(str(int(sub_mask[i])&int(ipaddr[i])))
	
	return ".".join(res)

	
#all operations for classless
		
def classless():
	print("******CLASSLESS********")	
	try:
		#ip_net_id=input("Enter net id(Classless notation)===")
		temp=input("Enter IP Address to assign to this machine(expected to give prefix length here itself eg.ipaddr/pref_length)===")
		no_of_subnets=int(input("enter No of subnets u want to make==")) 
		n=math.ceil(math.log(no_of_subnets,2))
		
		
		
		
		l=temp.split('/');
		ip_addr=l[0]
		try:
			prefix_length=l[1]
		except Exception:
			print("Looks like u have not given prefix length!")
			exit()
		
		ip_net=ipaddress.IPv4Network(ip_addr);
		
		mask=subnet_mask_classless(int(prefix_length))
	
		ip_net_id=find_net_id_classless(ip_addr,mask)	
			
		ip_net_id=ip_net_id+"/"+prefix_length
		
		try:
			
				
			network=ipaddress.IPv4Network(ip_net_id)              #Network not address (Ipv4)
		except Exception:
			print("Cannot make subnets due to inconsistency!!")
		else:
			changeip(ip_addr,mask)
			print("Extracting net id from given ip address and calculated subnet mask")
			print("********Network Details****************")
			print("Net id=="+ip_net_id)
			
			subnets_gr=list(network.subnets(n))
			print("Subnet mask==%s"%(network.netmask))
			print("\n\n************Subnets***************")
			subNet(ip_net_id,subnets_gr,no_of_subnets)
			ping(ip_addr,subnets_gr)
			

		
	except Exception:
		print("Enter proper netid next time!!")
		


    
if __name__=="__main__":
	
	print("Before running the program check if u r superuser(required for changing ip)")
	classful()	
	#print("******MENU********")
	#print("1.Classful \n2.Classless")
	#menu=int(input("Enter your choice=="))
	#if(menu==1):
		
	#elif(menu==2):
	#	classless()
	#else:
	#	print("Invalid menu no")
	
	#os.system("sudo ifconfig ens33 192.168.230.128 netmask 255.255.255.0")
	
	
	
	
	'''	
    to change ip:
    os.system('sudo ifconfig eth0 down')
os.system('sudo ifconfig eth0 192.168.1.10')
os.system('sudo ifconfig eth0 up')

    prints list of interface
    os.listdir('/sys/class/net/')
    
    
    to print current ip
    os.system('ip -4 addr show ens33 | grep -oP "(?<=inet\s)\d+(\.\d+){3}"')


	'''
