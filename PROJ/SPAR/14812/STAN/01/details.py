
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14812"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14812"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard Turbo')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard_Turbo')
    newPart['gitName'].append('RedBoard_Turbo')
    newPart['eagleBoard'].append('/Hardware/RedBoard_Turbo.brd')
    newPart['eagleSchem'].append('/Hardware/RedBoard_Turbo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

