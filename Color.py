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
            'User defined':6,#110           
            'White':6 #111
        }
        self.ColorCode=switcher.get(color_name,0)
        self.ColorName=color_name
        
    def printColorName(self):
        print(self.ColorName)


