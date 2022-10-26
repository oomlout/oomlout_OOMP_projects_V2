
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15951"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15951"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Step')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Step')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Step')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Step/Hardware/Qwiic-Step.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Step/Hardware/Qwiic-Step.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

