
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16476"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16476"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroPressure Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroPressure_Sensor')
    newPart['gitName'].append('MicroPressure_Sensor')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroPressure_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroPressure_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

