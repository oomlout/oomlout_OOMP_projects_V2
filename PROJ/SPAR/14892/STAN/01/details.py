
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14892"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14892"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/ePaper')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/ePaper')
    newPart['gitName'].append('https://github.com/sparkfunX/ePaper')
    newPart['eagleBoard'].append('sourceFiles/git/ePaper/1.54in display/hardware/1.54in.brd')
    newPart['eagleSchem'].append('sourceFiles/git/ePaper/1.54in display/hardware/1.54in.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

