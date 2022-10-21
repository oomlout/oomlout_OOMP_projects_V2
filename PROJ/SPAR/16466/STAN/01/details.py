
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16466"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16466"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Environmental Sensor Breakout BME680')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Environmental_Sensor_Breakout_BME680')
    newPart['gitName'].append('SparkFun_Environmental_Sensor_Breakout_BME680')
    newPart['eagleBoard'].append('/Hardware/Qwiic Environmental BME680.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Environmental BME680.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

