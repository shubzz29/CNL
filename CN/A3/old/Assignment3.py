from math import log, ceil
import ipaddress as ip
import os

def netFun():
    ipAddress = input("Enter the IpAddress you want to assign to the machine \n")
    
    netId = ""
    Smask = ""
    numSubnet = int(input("Enter the number of Subnetworks"))
    numList = ipAddress.split('.')
    numList = [int(i) for i in numList]
    #print(numList)
    netIdList = numList
    mask = {'A': [255, 0, 0, 0], 'B': [255, 255, 0, 0], 'C': [255, 255, 255, 0], 'D': [255, 255, 255, 255]}
    n = int(ceil((log(numSubnet, 2))))  # For number of bits
    if numList[0] in range(128):
        print("Class A")
        temp = 0
        if n in range(8):
            for i in range(n):
                temp = temp + 2 ** (7 - i)
                mask['A'][1] = temp
        elif n in range(8, 16):
            mask['A'][1] = 255
            for i in range(n - 8):
                temp = temp + 2 ** (7 - i)
            mask['A'][2] = temp
        elif n in range(16, 24):
            mask['A'][1] = 255
            mask['A'][2] = 255
            for i in range(n - 16):
                temp = temp + 2 ** (7 - i)
            mask['A'][3] = temp
        else:
            mask['A'][1] = 255
            mask['A'][2] = 255
            mask['A'][3] = 255
       # calcIp(ipAddress, n, numSubnet)
        netIdList[1] = 0
        netIdList[2] = 0
        netIdList[3] = 0
        print("Net ID is :: " + netId +"/"+ str(8 + n))
        netId = '.'.join(str(x) for x in netIdList)
        netId += "/8"
        Smask = '.'.join(str(x) for x in mask['A'])
        print("Subnet Mask is :: " + Smask)


    elif numList[0] < 192:
        print("Class B")
        temp = 0
        if n in range(8):
             for i in range(n):
                 temp = temp + 2 ** (7 - i)
             mask['B'][2] = temp
        elif n in range(8, 16):
            mask['B'][2] = 255
            for i in range(n-8):
                temp = temp + 2**(7-i)
            mask['B'][3] = temp
        else:
            mask['B'][2] = 255
            mask['B'][3] = 255

        netIdList[2] = 0
        netIdList[3] = 0
        netId = '.'.join(str(x) for x in netIdList)
        print("Net ID is :: " + netId +"/"+ str(16 + n))
        netId += "/16"
        Smask = '.'.join(str(x) for x in mask['B'])
        print("Subnet Mask is :: " + '.'.join(str(x) for x in mask['B']))

    elif numList[0] < 224:
        print("Class C")
        temp = 0
        if n in range(8):
            for i in range(n):
                temp = temp + 2 ** (7 - i)
            mask['C'][3] = temp
        else:
            mask['C'][3] = 255

        #netIdList[2] = 0
        netIdList[3] = 0
        netId = '.'.join(str(x) for x in netIdList)
        print("Net ID is :: " + netId +"/"+ str(24 + n))
        netId += "/24"
        Smask = '.'.join(str(x) for x in mask['C'])
        print("Subnet Mask is :: " + '.'.join(str(x) for x in mask['C']))

    else:

        print("Class D")
        netId = '.'.join(str(x) for x in netIdList)
        netId += "/32"
        Smask = '.'.join(str(x) for x in mask['D'])
        print("Subnet Mask is :: " + '.'.join(str(x) for x in mask['D']))
        print("Net ID is :: " + netId)
    calcIp(netId, n, numSubnet)
    #changeIp(ipAddress, Smask)


def calcIp(netId , n , numSubnets):
    ipAddObj = ip.IPv4Network(netId)
    subnet_list = list(ipAddObj.subnets(n))
    for i in subnet_list:
        netList = list(i.hosts())
        print("First Address is :: " + str(netList[0]) + "\nLast Address is :: " + str(netList[-1]))

def ping():
    hostIp = input("Enter the ipaddress you want to ping\n")
    response = os.system("ping -c 1 "+ hostIp)
    if response == 0:
        print("Ping is successful")
    else:
        print("Response is :: " + response)

def changeIp(ipAddress, sMask):

   os.system("sudo ifconfig wlan0 down")
   os.system("sudo ifconfig wlan0 " + ipAddress + " netmask " + sMask)
   os.system("sudo ifconfig wlan0 up")

netFun()
#ping()
