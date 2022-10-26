
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17354"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17354"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('nRF9160 Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/nRF9160_Thing_Plus')
    newPart['gitName'].append('nRF9160_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/nRF9160 Thing Plus.brd')
    newPart['eagleSchem'].append('/Hardware/nRF9160 Thing Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

