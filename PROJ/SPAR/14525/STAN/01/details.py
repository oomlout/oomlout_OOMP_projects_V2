
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14525"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14525"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard Edge')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard_Edge')
    newPart['gitName'].append('RedBoard_Edge')
    newPart['eagleBoard'].append('/Hardware/modified_eagle_files/RedBoard.brd')
    newPart['eagleSchem'].append('/Hardware/modified_eagle_files/RedBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

