
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14748"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14748"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic UV VEML6075')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_UV_VEML6075')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_UV_VEML6075')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_UV_VEML6075/Hardware/Qwiic_UV_Sensor_VEML6075.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_UV_VEML6075/Hardware/Qwiic_UV_Sensor_VEML6075.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

