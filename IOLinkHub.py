import socket
import sys
from IoLinkCommand import *


class IOLinkHub:
    __Socket_instance = None 
    __IoMasterIP='192.168.33.249'
    __recievePort = 2000
    __transmitPort = 1999
    __localAddresIp = '192.168.33.250'
    Lamps = {}
    def __init__(self,localAddressIp,IoMasterIP):
        self.__localAddresIp=localAddressIp
        self.__IoMasterIP=IoMasterIP
        try:
            self.__Socket_instance=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.__Socket_instance.bind((self.__localAddresIp,self.__recievePort))
        except socket.error:
            print('Connection failed')
            sys.exit()
        self.__sendConnectCmd()
        


    def __sendConnectCmd(self):
        self.__Socket_instance.sendto(CreateConnectCommand(),(self.__IoMasterIP,self.__transmitPort))
    
    def AddLampsOnPort(self, Port,Lamp):
        self.Lamps[Port]=Lamp

    def SendData(self,data):
        self.__Socket_instance.sendto(data,(self.__IoMasterIP, self.__transmitPort))
        #Receive

    def SendProcessDataOnPort(self,port,data):
        to_send =CreateWriteProcessDataCommand(port,data)
        print('Proccess data send: ')
        PrintByteArray(to_send)
        self.__Socket_instance.sendto(to_send,(self.__IoMasterIP, self.__transmitPort))
        self.__Socket_instance.recvfrom(1024)

    def WriteRequest(self,port,index,subindex,data):
        self.__Socket_instance.sendto(CreateWriteRequestCommand(port,index,subindex,data),(self.__IoMasterIP, self.__transmitPort))


    
        
