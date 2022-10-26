
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14767"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14767"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Pressure LPS25HB')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Pressure-LPS25HB')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Pressure-LPS25HB')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Pressure-LPS25HB/Hardware/Qwiic Pressure Sensor - LPS25HB.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Pressure-LPS25HB/Hardware/Qwiic Pressure Sensor - LPS25HB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

