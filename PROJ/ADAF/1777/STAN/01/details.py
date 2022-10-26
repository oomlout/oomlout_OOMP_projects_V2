
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1777"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1777"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Si1145 Light Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Si1145-Light-Sensor-PCB')
    newPart['gitName'].append('Adafruit-Si1145-Light-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit Si1145 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit Si1145 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

