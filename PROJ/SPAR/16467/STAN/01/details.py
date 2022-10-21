
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16467"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16467"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Humidity Sensor SHTC3')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Humidity_Sensor_SHTC3')
    newPart['gitName'].append('SparkFun_Humidity_Sensor_SHTC3')
    newPart['eagleBoard'].append('/Hardware/SHTC3 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SHTC3 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

