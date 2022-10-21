
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3296"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3296"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('DS1307 breakout board')
    newPart['gitRepo'].append('https://github.com/adafruit/DS1307-breakout-board')
    newPart['gitName'].append('DS1307-breakout-board')
    newPart['eagleBoard'].append('/DS1307 Rev B.brd')
    newPart['eagleSchem'].append('/DS1307 Rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

