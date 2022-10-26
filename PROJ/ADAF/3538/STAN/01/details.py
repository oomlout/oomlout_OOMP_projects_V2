
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3538"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3538"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AMG8833 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AMG8833-Breakout-PCB')
    newPart['gitName'].append('Adafruit-AMG8833-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit AMG8833 FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit AMG8833 FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

