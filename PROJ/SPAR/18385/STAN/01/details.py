
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18385"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18385"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic CO2 Sensor STC31')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_CO2_Sensor-STC31')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_CO2_Sensor-STC31')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_CO2_Sensor-STC31/Hardware/STC31 Breakout.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_CO2_Sensor-STC31/Hardware/STC31 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

