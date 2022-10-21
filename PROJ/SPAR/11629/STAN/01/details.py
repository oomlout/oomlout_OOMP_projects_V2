
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11629"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11629"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial7SegmentDisplay')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial7SegmentDisplay')
    newPart['gitName'].append('Serial7SegmentDisplay')
    newPart['eagleBoard'].append('/hardware/Serial-7-Segment-Display.brd')
    newPart['eagleSchem'].append('/hardware/Serial-7-Segment-Display.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

