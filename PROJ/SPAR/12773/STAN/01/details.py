
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12773"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12773"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CryptoCape')
    newPart['gitRepo'].append('https://github.com/sparkfun/CryptoCape')
    newPart['gitName'].append('CryptoCape')
    newPart['eagleBoard'].append('/Hardware/cryptocape.brd')
    newPart['eagleSchem'].append('/Hardware/cryptocape.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

