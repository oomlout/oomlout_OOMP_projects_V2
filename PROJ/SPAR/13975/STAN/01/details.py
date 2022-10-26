
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13975"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13975"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Safe Cracker')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Safe_Cracker')
    newPart['gitName'].append('https://github.com/sparkfunX/Safe_Cracker')
    newPart['eagleBoard'].append('sourceFiles/git/Safe_Cracker/Hardware/Safe Cracker Shield.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Safe_Cracker/Hardware/Safe Cracker Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

