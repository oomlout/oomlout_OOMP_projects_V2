
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19217"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19217"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Thing Plus Dual Port Logging Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Thing_Plus_Dual-Port_Logging_Shield')
    newPart['gitName'].append('Thing_Plus_Dual-Port_Logging_Shield')
    newPart['eagleBoard'].append('/Hardware/Dual-Port_Logging_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Dual-Port_Logging_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

