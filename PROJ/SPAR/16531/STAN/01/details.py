
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16531"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16531"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Air Quality Sensor SGP30')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Air_Quality_Sensor-SGP30')
    newPart['gitName'].append('SparkFun_Air_Quality_Sensor-SGP30')
    newPart['eagleBoard'].append('/Hardware/SGP30 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SGP30 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

