
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15838"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15838"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic ATECC608A')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_ATECC608A')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_ATECC608A')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_ATECC608A/Hardware/Qwiic_ATECC608A.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_ATECC608A/Hardware/Qwiic_ATECC608A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

