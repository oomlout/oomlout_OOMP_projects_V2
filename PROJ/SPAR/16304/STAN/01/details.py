
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16304"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16304"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Temperature Sensor TMP102 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/Temperature_Sensor_TMP102_Qwiic')
    newPart['gitName'].append('Temperature_Sensor_TMP102_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TMP102_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TMP102_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

