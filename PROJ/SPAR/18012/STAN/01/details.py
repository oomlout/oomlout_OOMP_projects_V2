
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18012"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18012"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic MultiPort')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_MultiPort')
    newPart['gitName'].append('Qwiic_MultiPort')
    newPart['eagleBoard'].append('/Hardware/Qwiic_MultiPort.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_MultiPort.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

