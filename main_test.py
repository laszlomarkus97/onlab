from BallufLamp import BallufLamp
from IOLinkHub import IOLinkHub
from Color import *

hub = IOLinkHub('192.168.33.250','192.168.33.249')
for PortNo in range(0, 8):   
    BallufLamp().AttachToHub(hub,PortNo)

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetAllSegmentRed()

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetUserSpecifiedColor(RGB_Color(255,0,154))






