
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16329"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16329"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun u blox NEO M8U')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_u-blox_NEO-M8U')
    newPart['gitName'].append('SparkFun_u-blox_NEO-M8U')
    newPart['eagleBoard'].append('/Hardware/SparkFun NEO-M8U.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun NEO-M8U.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

