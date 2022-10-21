
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16677"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16677"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Refrigeration Gas Sensor ZMOD4450 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Refrigeration_Gas_Sensor_ZMOD4450_Qwiic')
    newPart['gitName'].append('SparkFun_Refrigeration_Gas_Sensor_ZMOD4450_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun Refrigerator Gas Sensor - ZMOD4450.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun Refrigerator Gas Sensor - ZMOD4450.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

