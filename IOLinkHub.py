import socket
import sys
from IoLinkCommand import *


class IOLinkHub:
    __Socket_instance = None 
    __IoMasterIP='192.168.1.1'
    __recievePort = 2000
    __transmitPort = 1999
    __localAddresIp = '192.168.0.10'
    Lamps = {}
    def __init__(self,localAddressIp):
        __localAddresIp=localAddressIp
        try:
            __Socket_instance=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            __Socket_instance.bind((self.__localAddresIp,self.__recievePort))
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
        self.__Socket_instance.sendto(CreateWriteProcessDataCommand(port,data),(self.__IoMasterIP, self.__transmitPort))

    def WriteRequest(self,port,index,subindex,data):
        self.__Socket_instance.sendto(CreateWriteRequestCommand(port,index,subindex,data),(self.__IoMasterIP, self.__transmitPort))


    
        
