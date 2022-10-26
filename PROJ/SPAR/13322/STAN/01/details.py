
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13322"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13322"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Soil Moisture Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/Soil_Moisture_Sensor')
    newPart['gitName'].append('Soil_Moisture_Sensor')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Soil_Moisture_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Soil_Moisture_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

