
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12037"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12037"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Binary Blaster')
    newPart['gitRepo'].append('https://github.com/sparkfun/Binary_Blaster')
    newPart['gitName'].append('Binary_Blaster')
    newPart['eagleBoard'].append('/Hardware/Binary_Blaster.brd')
    newPart['eagleSchem'].append('/Hardware/Binary_Blaster.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

