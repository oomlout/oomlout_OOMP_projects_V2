
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3435"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3435"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TPL5110 Power Timer Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TPL5110-Power-Timer-Breakout-PCB')
    newPart['gitName'].append('Adafruit-TPL5110-Power-Timer-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit TPL5110.brd')
    newPart['eagleSchem'].append('/Adafruit TPL5110.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

