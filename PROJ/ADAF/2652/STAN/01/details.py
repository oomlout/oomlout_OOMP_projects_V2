
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2652"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2652"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BME280 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BME280-Breakout-PCB')
    newPart['gitName'].append('Adafruit-BME280-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit BME280.brd')
    newPart['eagleSchem'].append('/Adafruit BME280.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

