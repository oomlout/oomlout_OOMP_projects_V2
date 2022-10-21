
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2635"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit HDC1008 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-HDC1008-Breakout-PCB')
    newPart['gitName'].append('Adafruit-HDC1008-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit HDC1008.brd')
    newPart['eagleSchem'].append('/Adafruit HDC1008.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

