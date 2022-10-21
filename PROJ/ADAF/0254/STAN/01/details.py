
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0254"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroSD breakout board')
    newPart['gitRepo'].append('https://github.com/adafruit/MicroSD-breakout-board')
    newPart['gitName'].append('MicroSD-breakout-board')
    newPart['eagleBoard'].append('/microsd.brd')
    newPart['eagleSchem'].append('/microsd.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

