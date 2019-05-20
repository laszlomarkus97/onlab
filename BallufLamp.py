import IOLinkHub 
from IoLinkCommand import *
from utills import *
from BallufLampRegisters import *
from Segments import *

class BallufLamp:

    __ledData=None
    __ProcessData=None
    __Hub = None
    __Port = None

    def AttachToHub(self,Hub,Port):
        self.__Hub=Hub
        self.__Port=Port
        Hub.AddLampsOnPort(Port,self)


    #stateless functions

    def SetMode(self,mode):
        ModeIndex = 0x00
        ModeSubIndex = 0x00
        switcher = {
            'Segment':0,    #000
            'Level':1,  #001
            'Runlight':2,    #010
            'Flexible':3, #011
        }
        mode_data = NumberToByteArray(switcher.get(mode,0))
        data = CreateWriteRequestCommand(self.__Port,ModeIndex,ModeSubIndex,mode_data)
        self.__Hub.SendData(data)

    def SetSegments(self, Segments):
        temp_processData= Segments.returnProcessData()
        self.__Hub.SendProcessDataOnPort(self.__Port,temp_processData)
    
    def SetUserSpecifiedColor(self,port,ColorRGB):
        temp_data=ColorRGB.returnByteArrayWithoutOnOff()
        self.__Hub.WriteRequest(port,BallufLampRegister.Usercolor,0,temp_data)
        
    def SetAllSegmentWhite(self):
        whiteSeg=Segments('White','White','White','White','White')
        temp_processData= whiteSeg.returnProcessData()
        self.__Hub.SendProcessDataOnPort(self.__Port,temp_processData)


    def SetLeds(self, Leds):
        pass
    

    #state functions

    def SetSegment(self, SegmentNumber,Color):
        pass
    
    def SetLedColor(self, LedNo,RGB,On=255,Off=0):
        pass

    def SetLed(self,LedNo,enable):
        pass
    
    