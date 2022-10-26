
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12634"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12634"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Simon Tilts')
    newPart['gitRepo'].append('https://github.com/sparkfun/Simon_Tilts')
    newPart['gitName'].append('Simon_Tilts')
    newPart['eagleBoard'].append('/Hardware/Simon_Tilts.brd')
    newPart['eagleSchem'].append('/Hardware/Simon_Tilts.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

