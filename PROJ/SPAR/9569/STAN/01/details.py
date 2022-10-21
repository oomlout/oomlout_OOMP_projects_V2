
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9569"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9569"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Humidity Sensor Breakout HIH 4030')
    newPart['gitRepo'].append('https://github.com/sparkfun/Humidity_Sensor_Breakout-HIH-4030')
    newPart['gitName'].append('Humidity_Sensor_Breakout-HIH-4030')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Humidity_Sensor_Breakout-HIH-4030.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Humidity_Sensor_Breakout-HIH-4030.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

