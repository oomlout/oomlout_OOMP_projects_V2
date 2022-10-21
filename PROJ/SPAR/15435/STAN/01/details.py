
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15435"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15435"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XBee3 Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/XBee3_Thing_Plus')
    newPart['gitName'].append('XBee3_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/XBEE3_Thing_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/XBEE3_Thing_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

