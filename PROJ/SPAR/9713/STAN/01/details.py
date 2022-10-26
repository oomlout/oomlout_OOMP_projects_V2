
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9713"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9713"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('UBW32')
    newPart['gitRepo'].append('https://github.com/sparkfun/UBW32')
    newPart['gitName'].append('UBW32')
    newPart['eagleBoard'].append('/Hardware/UBW32_MX460_v262.brd')
    newPart['eagleSchem'].append('/Hardware/UBW32_MX460_v262.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

