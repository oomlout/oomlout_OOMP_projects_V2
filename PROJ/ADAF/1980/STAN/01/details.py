
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1980"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1980"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TSL2561 breakout board PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/TSL2561-breakout-board-PCB')
    newPart['gitName'].append('TSL2561-breakout-board-PCB')
    newPart['eagleBoard'].append('/TSL2561 Stemma.brd')
    newPart['eagleSchem'].append('/TSL2561 Stemma.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

