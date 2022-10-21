
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15100"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15100"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB C Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB-C-Breakout')
    newPart['gitName'].append('USB-C-Breakout')
    newPart['eagleBoard'].append('/Hardware/USB-C-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/USB-C-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

