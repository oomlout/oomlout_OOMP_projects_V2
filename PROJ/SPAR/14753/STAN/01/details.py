
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14753"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14753"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/RGB Panel Mega Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/RGB_Panel_Mega_Shield')
    newPart['gitName'].append('https://github.com/sparkfunX/RGB_Panel_Mega_Shield')
    newPart['eagleBoard'].append('sourceFiles/git/RGB_Panel_Mega_Shield/Hardware/RGB 32x64 Shield for Arduino Mega.brd')
    newPart['eagleSchem'].append('sourceFiles/git/RGB_Panel_Mega_Shield/Hardware/RGB 32x64 Shield for Arduino Mega.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

