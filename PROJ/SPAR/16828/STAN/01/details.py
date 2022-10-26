
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16828"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16828"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ArtemisDevKit')
    newPart['gitRepo'].append('https://github.com/sparkfun/ArtemisDevKit')
    newPart['gitName'].append('ArtemisDevKit')
    newPart['eagleBoard'].append('/hardware/ArtemisDevKit.brd')
    newPart['eagleSchem'].append('/hardware/ArtemisDevKit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

