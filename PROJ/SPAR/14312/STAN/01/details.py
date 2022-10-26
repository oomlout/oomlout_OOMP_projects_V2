
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14312"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic GPS TitanX1')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_GPS-TitanX1')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_GPS-TitanX1')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_GPS-TitanX1/Hardware/Qwiic GPS - Titan X1.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_GPS-TitanX1/Hardware/Qwiic GPS - Titan X1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

