
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13975"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13975"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard')
    newPart['gitName'].append('RedBoard')
    newPart['eagleBoard'].append('/Hardware/RedBoard.brd')
    newPart['eagleSchem'].append('/Hardware/RedBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

