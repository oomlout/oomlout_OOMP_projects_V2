
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15794"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15794"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Pi SHIM')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Pi_SHIM')
    newPart['gitName'].append('Qwiic_Pi_SHIM')
    newPart['eagleBoard'].append('/Hardware/Qwiic Pi SHIM.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Pi SHIM.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

