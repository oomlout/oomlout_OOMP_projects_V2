
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14449"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14449"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Variable Load')
    newPart['gitRepo'].append('https://github.com/sparkfun/Variable_Load')
    newPart['gitName'].append('Variable_Load')
    newPart['eagleBoard'].append('/Hardware/Variable_Load.brd')
    newPart['eagleSchem'].append('/Hardware/Variable_Load.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

