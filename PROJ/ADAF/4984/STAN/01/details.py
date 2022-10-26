
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4984"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4984"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DVI Breakout Board PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DVI-Breakout-Board-PCB')
    newPart['gitName'].append('Adafruit-DVI-Breakout-Board-PCB')
    newPart['eagleBoard'].append('/Adafruit DVI Breakout board.brd')
    newPart['eagleSchem'].append('/Adafruit DVI Breakout board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

