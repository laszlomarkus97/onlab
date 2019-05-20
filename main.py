from BallufLamp import BallufLamp
from IOLinkHub import IOLinkHub 

hub = IOLinkHub('192.168.0.10')


for PortNo in range(0, 8):   
    BallufLamp().AttachToHub(hub,PortNo)






