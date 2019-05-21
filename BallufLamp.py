import IOLinkHub 
from IoLinkCommand import*
from utills import *
from BallufLampRegisters import*
from Segments import*
import time

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
        ModeIndex = BallufLampRegister.Mode_Index
        ModeSubIndex = 0x00
        switcher = {
            'Segment':0,    #000
            'Level':1,  #001
            'Runlight':2,    #010
            'Flexible':3, #011
        }
        mode_data = NumberToByteArray(switcher.get(mode,0))
        self.__Hub.WriteRequest(self.__Port,ModeIndex,ModeSubIndex,mode_data)
       
        time.sleep(0.50)
        #Reset Process Data
        if(switcher.get(mode,0)==3):
            switch_on_data = bytearray.fromhex('ff ff ff')
            self.__Hub.SendProcessDataOnPort(self.__Port,switch_on_data)
        time.sleep(0.50)


    def SetSegments(self, Segments):
        temp_processData= Segments.returnProcessData()
        self.__Hub.SendProcessDataOnPort(self.__Port,temp_processData)
        time.sleep(0.20)
    
    def SetUserSpecifiedColor(self,ColorRGB):
        temp_data=ColorRGB.returnByteArrayWithoutOnOff()
        self.__Hub.WriteRequest(self.__Port,BallufLampRegister.Usercolor,0,temp_data)
        time.sleep(0.20)
        
    def SetSegmentsToTestThingWorx(self):
        whiteSeg=Segments(Color('Red'),Color('User_defined'),Color('User_defined'),Color('User_defined'),Color('Red'))
        temp_processData= whiteSeg.returnProcessData()
        self.__Hub.SendProcessDataOnPort(self.__Port,temp_processData)
        time.sleep(0.20)


    def SetLedColor(self,LedNo,Color):
        print('Led no:' +str(LedNo))
        LedNo=LedNo-1
        if(LedNo>=20):
            print('led no out of range')
            return
        Led_Address= LedNo+BallufLampRegister.Led_color_base
        temp_data = Color.returnByteArrayWithOnOff()
        self.__Hub.WriteRequest(self.__Port,Led_Address,0,temp_data)
        time.sleep(0.20)

    


    
    