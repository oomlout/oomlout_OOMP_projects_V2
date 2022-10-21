
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15733"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15733"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun u Blox NEO M9N')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_u-Blox_NEO_M9N')
    newPart['gitName'].append('SparkFun_u-Blox_NEO_M9N')
    newPart['eagleBoard'].append('/Hardware/SparkFun GPS NEO_M9N_Chip_Antenna/SparkFun GPS NEO_M9N_ANT.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun GPS NEO_M9N_Chip_Antenna/SparkFun GPS NEO_M9N_ANT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

