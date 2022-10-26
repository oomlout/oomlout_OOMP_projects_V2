
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14532"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14532"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Micro OLED')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Micro_OLED')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Micro_OLED')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Micro_OLED/Hardware/Qwiic_OLED_Breakout.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Micro_OLED/Hardware/Qwiic_OLED_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

