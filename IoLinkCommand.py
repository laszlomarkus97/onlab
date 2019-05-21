import sys
from utills import *
from IoLinkCommandDefs import *


#@brief Create an IOLinkComand
#@return bytearray
def CreateHubCommand(Command, Port, Data):
    lenOfPacket = 2+1+1+1+len(Data)
    lenOfPacket_bytes = lenOfPacket.to_bytes(1,sys.byteorder)
    port_bytes = Port.to_bytes(1,sys.byteorder)
    cmd_bytes = Command.to_bytes(1, sys.byteorder)
    communication_type_bytes = CommunicationType.to_bytes(1, sys.byteorder)
    ret = bytearray(lenOfPacket_bytes)+bytearray.fromhex('00')+bytearray(communication_type_bytes)+bytearray(cmd_bytes)+bytearray(port_bytes)+Data
    print('command')
    PrintByteArray(ret)
    return ret

#@brief Create a connect command
#@return bytearray
def CreateConnectCommand():
    data = bytearray.fromhex('00')+bytearray('IO-Link-Device-Tool','utf-8')+bytearray.fromhex('00')
    return CreateHubCommand(CMD_CONNECT,0,data)

#@brief Create a Read Request Command
#@param Port
#@param Index
#@param Subindex
#@note using CMD_ALREADREQ 
#@note works only for 255 or lower index and subindex
#@return bytearray
def CreateReadRequestCommand(Port,Index,Subindex):
    data = NumberToByteArray(Index)+bytearray('00')+NumberToByteArray(Subindex)
    return CreateHubCommand(CMD_ALREADREQ,Port,data)

#@brief Create a Write Request Command
#@param Port
#@param Index
#@param Subindex
#@param Data bytearray 
#@note using CMD_ALWRITEREQ 
#@note works only for 255 or lower index and subindex
#@return bytearray
def CreateWriteRequestCommand(Port,Index,Subindex,Data):
    data_len = len(Data)
    data_all = NumberToByteArray(Index)+bytearray.fromhex('00')+NumberToByteArray(Subindex)+NumberToByteArray(data_len)+Data
    return CreateHubCommand(CMD_ALWRITEREQ,Port,data_all)


#@brief Create Read Proccess Data Command
#@param Port
#@note using CMD_READPROCESSDATA 
#@return bytearray
def CreateReadProccessDataCommand(Port):
    data = bytearray(0)
    return CreateHubCommand(CMD_READPROCESSDATA,Port,data)

#@brief Create Write Process Data Command
#@param Port
#@param Data
#@note using CMD_WRITEPROCESSDATA 
#@return bytearray
def CreateWriteProcessDataCommand(Port,Data):
    ret = CreateHubCommand(CMD_WRITEPROCESSDATA,Port,Data)
    return ret
##TODO ___________________

#@brief Create a Write Request Command
#@return bytearray
def CreateSetPortConfigCommand():
    print('NOT implemented function call')






