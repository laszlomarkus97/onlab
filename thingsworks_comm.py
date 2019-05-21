from flask import Flask
from flask import request
from BallufLamp import BallufLamp
from IOLinkHub import IOLinkHub
from Color import *

hub = IOLinkHub('192.168.33.250','192.168.33.249')
for PortNo in range(0, 8):   
    BallufLamp().AttachToHub(hub,PortNo)

for PortNo in range(0, 8):
    hub.Lamps[PortNo].SetAllSegmentRed()
    
app = Flask(__name__)


@app.route('/<lamp_id>/<color>')
def home(lamp_id, color):
    print(lamp_id, )
    red, green, blue = color.split('_')
    color1 = RGB_Color(int(red), int(green), int(blue))
    hub.Lamps[int(lamp_id)].SetUserSpecifiedColor(color1)
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='32345')
