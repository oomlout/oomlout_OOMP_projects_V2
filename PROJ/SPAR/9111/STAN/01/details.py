
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9111"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9111"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XBee Explorer Serial')
    newPart['gitRepo'].append('https://github.com/sparkfun/XBee_Explorer_Serial')
    newPart['gitName'].append('XBee_Explorer_Serial')
    newPart['eagleBoard'].append('/Hardware/SparkFun_XBee_Serial_Explorer.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_XBee_Serial_Explorer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

