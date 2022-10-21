
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3246"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3246"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Mini Analog Thumbstick Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Mini-Analog-Thumbstick-Breakout-PCB')
    newPart['gitName'].append('Adafruit-Mini-Analog-Thumbstick-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit Mini Analog Thumbstick.brd')
    newPart['eagleSchem'].append('/Adafruit Mini Analog Thumbstick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

