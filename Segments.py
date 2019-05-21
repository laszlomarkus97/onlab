from Color import *


class Segments:
    Seg = [None]*5

    def __init__(self, SegColor1, SegColor2, SegColor3, SegColor4, SegColor5):
        self.Seg[0] = SegColor1
        self.Seg[1] = SegColor2
        self.Seg[2] = SegColor3
        self.Seg[3] = SegColor4
        self.Seg[4] = SegColor5
    
    def modifySegColor(self,SegNo,Color):
        if(SegNo<5):
            self.Seg[SegNo-1]=Color
        else:
            print('segment index out of range')

    def returnProcessData(self):
        temp_processData = 0
        for x in range(0, 5):
            temp_processData = temp_processData | (
                self.Seg[x].ColorCode << Segment(x+1).get_offset())
        return bytearray(temp_processData.to_bytes(3,byteorder='big'))[0:3]


class Segment:
    offset = 0

    def __init__(self, number_of_segment):
        switcher = {
            1: 16,
            2: 20,
            3: 8,
            4: 12,
            5: 0
        }
        self.offset = switcher.get(number_of_segment)

    def get_offset(self):
        return self.offset


PrintByteArray(Segments(Color('Red'), Color('Red'), Color('Red'),
               Color('Red'), Color('Red')).returnProcessData())
