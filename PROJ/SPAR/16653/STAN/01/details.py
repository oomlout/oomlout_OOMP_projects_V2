
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16653"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16653"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Top pHat')
    newPart['gitRepo'].append('https://github.com/sparkfun/Top_pHat')
    newPart['gitName'].append('Top_pHat')
    newPart['eagleBoard'].append('/Hardware/Top pHAT.brd')
    newPart['eagleSchem'].append('/Hardware/Top pHAT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

