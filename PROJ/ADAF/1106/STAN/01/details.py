
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1106"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1106"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TIMESQUARE DIY Watch Kit')
    newPart['gitRepo'].append('https://github.com/adafruit/TIMESQUARE-DIY-Watch-Kit')
    newPart['gitName'].append('TIMESQUARE-DIY-Watch-Kit')
    newPart['eagleBoard'].append('/Adafruit_TIMESQUARE.brd')
    newPart['eagleSchem'].append('/Adafruit_TIMESQUARE.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

