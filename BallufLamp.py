import IOLinkHub 
from IoLinkCommand import*
from utills import *
from BallufLampRegisters import*
from Segments import*

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
    
    def SetUserSpecifiedColor(self,ColorRGB):
        temp_data=ColorRGB.returnByteArrayWithoutOnOff()
        self.__Hub.WriteRequest(self.__Port,BallufLampRegister.Usercolor,0,temp_data)
        
    def SetSegmentsToTestThingWorx(self):
        whiteSeg=Segments(Color('Red'),Color('User_defined'),Color('User_defined'),Color('User_defined'),Color('Red'))
        temp_processData= whiteSeg.returnProcessData()
        self.__Hub.SendProcessDataOnPort(self.__Port,temp_processData)


    def SetLeds(self, Leds):
        pass
    


    
    