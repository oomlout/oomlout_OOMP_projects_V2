
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17001"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic BMP388 Pressure Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_BMP388_Pressure_Sensor')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_BMP388_Pressure_Sensor')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_BMP388_Pressure_Sensor/Hardware/Qwiic_BMP388_Pressure_Sensor.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_BMP388_Pressure_Sensor/Hardware/Qwiic_BMP388_Pressure_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

