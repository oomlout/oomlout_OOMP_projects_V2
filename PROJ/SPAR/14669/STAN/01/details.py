
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14669"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14669"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BlackBoard')
    newPart['gitRepo'].append('https://github.com/sparkfun/BlackBoard')
    newPart['gitName'].append('BlackBoard')
    newPart['eagleBoard'].append('/Hardware/BlackBoard.brd')
    newPart['eagleSchem'].append('/Hardware/BlackBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

