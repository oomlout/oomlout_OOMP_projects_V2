
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1571"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1571"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit STMPE610 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-STMPE610-Breakout-PCB')
    newPart['gitName'].append('Adafruit-STMPE610-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit STMPE610.brd')
    newPart['eagleSchem'].append('/Adafruit STMPE610.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

