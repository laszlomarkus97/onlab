import IOLinkHub 
from IoLinkCommand import *
from utills import *

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

    def SetSegments(self, Segment):
        pass
    
    def SetUserSpecifiedColor(self,Color):
        pass
    
    def SetLeds(self, Leds):
        pass
    

    #state functions

    def SetSegment(self, SegmentNumber,Color):
        pass
    
    def SetLedColor(self, LedNo,RGB,On=255,Off=0):
        pass

    def SetLed(self,LedNo,enable):
        pass
    
    