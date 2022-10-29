
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19034"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19034"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic High Performance Magnetometer MMC5983MA')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_High_Performance_Magnetometer_MMC5983MA')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_High_Performance_Magnetometer_MMC5983MA')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_High_Performance_Magnetometer_MMC5983MA/Hardware/Qwiic_High_Performance_Magnetometer_X01.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_High_Performance_Magnetometer_MMC5983MA/Hardware/Qwiic_High_Performance_Magnetometer_X01.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

