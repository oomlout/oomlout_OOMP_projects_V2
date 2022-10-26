
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2857"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2857"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SHT31 Sensor Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SHT31-Sensor-Breakout-PCB')
    newPart['gitName'].append('Adafruit-SHT31-Sensor-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit SHT31 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit SHT31 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

