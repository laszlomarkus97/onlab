from BallufLamp import BallufLamp
from IOLinkHub import IOLinkHub
from Color import *
from Segments import *
import time

#Initialize. Must be done!!
hub = IOLinkHub('192.168.33.250','192.168.33.249')
for PortNo in range(0, 8):   
    BallufLamp().AttachToHub(hub,PortNo)

#If you want to change mode.. There are two supported mode
#Flexible :you can change all leds indepently
#Segment : leds organized into 5 segments
for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetMode('Flexible')
#For flexible mode led change  example  
for LedNo in range(1,21):
  for PortNo in range(0, 8):   
        hub.Lamps[PortNo].SetLedColor(LedNo,RGB_Color(0,50,111))
        
for LedNo in range(1,21):
  for PortNo in range(0, 8):   
        hub.Lamps[PortNo].SetLedColor(LedNo,RGB_Color(0,0,0))
        
#Change mode
for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetMode('Segment')

#Segment mode example
for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegments(Segments(Color('Red'),Color('Red'),Color('Red'),Color('Green'),Color('Red')))

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegments(Segments(Color('Red'),Color('Red'),Color('Red'),Color('Green'),Color('Green')))

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegments(Segments(Color('Red'),Color('Red'),Color('Red'),Color('Green'),Color('Blue')))

#In thingworx use case we use that configuration
for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegmentsToTestThingWorx()

#In that case you can change the middle three segment color to any RGB color
for Red in range(0, 253,30):
    for PortNo in range(0, 8):
        hub.Lamps[PortNo].SetUserSpecifiedColor(RGB_Color(Red,0,154))
        






