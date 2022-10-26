
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12761"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12761"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('microSD Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/microSD_Shield')
    newPart['gitName'].append('microSD_Shield')
    newPart['eagleBoard'].append('/Hardware/microSD_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/microSD_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

