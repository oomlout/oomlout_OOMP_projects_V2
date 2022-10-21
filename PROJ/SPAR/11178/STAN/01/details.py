
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11178"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11178"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BigTime')
    newPart['gitRepo'].append('https://github.com/sparkfun/BigTime')
    newPart['gitName'].append('BigTime')
    newPart['eagleBoard'].append('/Hardware/BigTime.brd')
    newPart['eagleSchem'].append('/Hardware/BigTime.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

