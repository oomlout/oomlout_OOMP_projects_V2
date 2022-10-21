
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13266"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13266"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MAX31855K Thermocouple Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MAX31855K_Thermocouple_Breakout')
    newPart['gitName'].append('MAX31855K_Thermocouple_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Thermocouple_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Thermocouple_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

