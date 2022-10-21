
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15423"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15423"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic Micro SAMD21E')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_Micro_SAMD21E')
    newPart['gitName'].append('SparkFun_Qwiic_Micro_SAMD21E')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_Micro_SAMD21E.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_Micro_SAMD21E.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

