
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15591"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Switch')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Switch')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Switch/Hardware/Qwiic_Switch.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Switch/Hardware/Qwiic_Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

