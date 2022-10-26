
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14686"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14686"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic IMU BNO080')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_IMU_BNO080')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_IMU_BNO080')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_IMU_BNO080/Documents/Qwiic_IMU_Bonobo.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_IMU_BNO080/Documents/Qwiic_IMU_Bonobo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

