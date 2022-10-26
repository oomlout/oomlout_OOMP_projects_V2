
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3595"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3595"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit APDS9960 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-APDS9960-Breakout-PCB')
    newPart['gitName'].append('Adafruit-APDS9960-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit APDS9960 Proximity Sensor.brd')
    newPart['eagleSchem'].append('/Adafruit APDS9960 Proximity Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

