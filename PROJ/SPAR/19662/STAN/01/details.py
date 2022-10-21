
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19662"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19662"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic Pressure Sensor BMP384')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_Pressure_Sensor_BMP384')
    newPart['gitName'].append('SparkFun_Qwiic_Pressure_Sensor_BMP384')
    newPart['eagleBoard'].append('/Hardware/Qwiic 1x1/BMP384 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic 1x1/BMP384 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

