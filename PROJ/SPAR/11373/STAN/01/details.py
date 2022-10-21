
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11373"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11373"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XBee Explorer Regulated')
    newPart['gitRepo'].append('https://github.com/sparkfun/XBee_Explorer_Regulated')
    newPart['gitName'].append('XBee_Explorer_Regulated')
    newPart['eagleBoard'].append('/Hardware/XBee-Regulated.brd')
    newPart['eagleSchem'].append('/Hardware/XBee-Regulated.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

