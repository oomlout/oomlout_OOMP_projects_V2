
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12013"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12013"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Touch Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Touch_Shield')
    newPart['gitName'].append('Touch_Shield')
    newPart['eagleBoard'].append('/Hardware/Touch_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Touch_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

