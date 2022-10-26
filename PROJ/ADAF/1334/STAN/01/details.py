
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1334"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1334"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TCS34725 Color Sensor Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TCS34725-Color-Sensor-Breakout-PCB')
    newPart['gitName'].append('Adafruit-TCS34725-Color-Sensor-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora TCS34725.brd')
    newPart['eagleSchem'].append('/Adafruit Flora TCS34725.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

