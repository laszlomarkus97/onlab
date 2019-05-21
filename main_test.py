from BallufLamp import BallufLamp
from IOLinkHub import IOLinkHub
from Color import *
from Segments import *
import time


hub = IOLinkHub('192.168.33.250','192.168.33.249')
for PortNo in range(0, 8):   
    BallufLamp().AttachToHub(hub,PortNo)

##for PortNo in range(0, 8):
##    hub.Lamps[PortNo].SetMode('Flexible')
##    
##for LedNo in range(1,21):
##  for PortNo in range(0, 8):   
##        hub.Lamps[PortNo].SetLedColor(LedNo,RGB_Color(0,50,111))
##        
##for LedNo in range(1,21):
##  for PortNo in range(0, 8):   
##        hub.Lamps[PortNo].SetLedColor(LedNo,RGB_Color(0,0,0))
        
##        
##for PortNo in range(0, 8):
##    hub.Lamps[PortNo].SetMode('Segment')

    
for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegments(Segments(Color('Red'),Color('Red'),Color('Red'),Color('Green'),Color('Red')))

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegments(Segments(Color('Red'),Color('Red'),Color('Red'),Color('Green'),Color('Green')))

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegments(Segments(Color('Red'),Color('Red'),Color('Red'),Color('Green'),Color('Blue')))

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetSegmentsToTestThingWorx()
    
for Red in range(0, 253,30):
    for PortNo in range(0, 8):
        hub.Lamps[PortNo].SetUserSpecifiedColor(RGB_Color(Red,0,154))
        






