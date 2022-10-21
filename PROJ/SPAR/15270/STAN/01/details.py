
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15270"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15270"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator log')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_log')
    newPart['gitName'].append('gator_log')
    newPart['eagleBoard'].append('/Hardware/GatorLog.brd')
    newPart['eagleSchem'].append('/Hardware/GatorLog.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

