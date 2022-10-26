
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13120"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13120"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MG2639 Cellular Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/MG2639_Cellular_Shield')
    newPart['gitName'].append('MG2639_Cellular_Shield')
    newPart['eagleBoard'].append('/Hardware/MG2639 Cellular Shield.brd')
    newPart['eagleSchem'].append('/Hardware/MG2639 Cellular Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

