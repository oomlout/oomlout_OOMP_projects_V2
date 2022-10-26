
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1895"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1895"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FRAM Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FRAM-Breakout-PCB')
    newPart['gitName'].append('Adafruit-FRAM-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit I2C FRAM.brd')
    newPart['eagleSchem'].append('/Adafruit I2C FRAM.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

