
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3190"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3190"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DRV8871 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DRV8871-Breakout-PCB')
    newPart['gitName'].append('Adafruit-DRV8871-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit DRV8871.brd')
    newPart['eagleSchem'].append('/Adafruit DRV8871.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

