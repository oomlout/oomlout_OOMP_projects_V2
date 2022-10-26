
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15106"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15106"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic GPS SAM M8Q')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_GPS_SAM-M8Q')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_GPS_SAM-M8Q')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_GPS_SAM-M8Q/Hardware/Qwiic GPS - Ublox SAM-M8Q.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_GPS_SAM-M8Q/Hardware/Qwiic GPS - Ublox SAM-M8Q.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

