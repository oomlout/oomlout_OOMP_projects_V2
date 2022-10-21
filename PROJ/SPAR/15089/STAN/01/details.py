
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15089"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15089"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun UV Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_UV_Sensor')
    newPart['gitName'].append('SparkFun_UV_Sensor')
    newPart['eagleBoard'].append('/Hardware/Qwiic_UV_Sensor_VEML6075.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_UV_Sensor_VEML6075.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

