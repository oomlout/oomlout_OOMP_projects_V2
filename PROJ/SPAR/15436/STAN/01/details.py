
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15436"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15436"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Ambient Sensor VEML6030')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Ambient_Sensor_VEML6030')
    newPart['gitName'].append('SparkFun_Ambient_Sensor_VEML6030')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Ambient_Light_Sensor_VEML6030.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Ambient_Light_Sensor_VEML6030.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

