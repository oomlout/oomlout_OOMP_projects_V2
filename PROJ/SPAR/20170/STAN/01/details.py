
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20170"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20170"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic Pressure Sensor BMP581')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_Pressure_Sensor_BMP581')
    newPart['gitName'].append('SparkFun_Qwiic_Pressure_Sensor_BMP581')
    newPart['eagleBoard'].append('/Hardware/Qwiic 1x1/SparkFun_Pressure_Sensor_BMP581_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic 1x1/SparkFun_Pressure_Sensor_BMP581_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

