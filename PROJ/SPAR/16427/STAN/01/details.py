
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16427"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16427"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Alphanumeric Display')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Alphanumeric_Display')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Alphanumeric_Display')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Alphanumeric_Display/Hardware/Qwiic_Alphanumeric_Display.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Alphanumeric_Display/Hardware/Qwiic_Alphanumeric_Display.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

