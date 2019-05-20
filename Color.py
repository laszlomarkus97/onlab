from utills import *

class Color:
    ColorCode = 0
    ColorName = 'No Color'
    def __init__(self, color_name):
        switcher = {
            'Off':0,    #000
            'Green':1,  #001
            'Red':2,    #010
            'Yellow':3, #011
            'Blue':4,   #100
            'Orange':5, #101
            'User_defined':6,#110           
            'White':7 #111
        }
        self.ColorCode=switcher.get(color_name,0)
        self.ColorName=color_name
    def printColorName(self):
        print(self.ColorName)

class RGB_Color:
    Red = 0
    Green = 0
    Blue = 0
    On= 255
    Off =0
    def __init__(self,red,green,blue,on=255,off=0):
        self.Red=red
        self.Green = green
        self.Blue = blue
        self.On= on
        self.Off =off

    def returnByteArrayWithOnOff(self):
        return NumberToByteArray(self.Red)+ NumberToByteArray(self.Green)+ NumberToByteArray(self.Blue)+NumberToByteArray(self.On)+NumberToByteArray(self.Off)
    def returnByteArrayWithoutOnOff(self):
        return NumberToByteArray(self.Red)+ NumberToByteArray(self.Green)+ NumberToByteArray(self.Blue)

            
   


