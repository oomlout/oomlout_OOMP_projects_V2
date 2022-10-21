
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13810"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13810"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('tsunami')
    newPart['gitRepo'].append('https://github.com/sparkfun/tsunami')
    newPart['gitName'].append('tsunami')
    newPart['eagleBoard'].append('/Hardware/tsunami.brd')
    newPart['eagleSchem'].append('/Hardware/tsunami.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

