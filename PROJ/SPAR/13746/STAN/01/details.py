
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13746"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13746"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Beefy 3')
    newPart['gitRepo'].append('https://github.com/sparkfun/Beefy_3')
    newPart['gitName'].append('Beefy_3')
    newPart['eagleBoard'].append('/Hardware/Beefy_3.brd')
    newPart['eagleSchem'].append('/Hardware/Beefy_3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

