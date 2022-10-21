
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12055"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12055"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TSL2561 Luminosity Sensor BOB')
    newPart['gitRepo'].append('https://github.com/sparkfun/TSL2561_Luminosity_Sensor_BOB')
    newPart['gitName'].append('TSL2561_Luminosity_Sensor_BOB')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TSL2561_Sensor_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TSL2561_Sensor_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

