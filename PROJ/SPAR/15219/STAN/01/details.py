
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15219"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15219"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Pulse Oximeter Heart Rate Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Pulse_Oximeter_Heart_Rate_Sensor')
    newPart['gitName'].append('SparkFun_Pulse_Oximeter_Heart_Rate_Sensor')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Pulse_Oximeter_Heart-Rate_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Pulse_Oximeter_Heart-Rate_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

