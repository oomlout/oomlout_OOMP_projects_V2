
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13183"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13183"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CryptoShield')
    newPart['gitRepo'].append('https://github.com/sparkfun/CryptoShield')
    newPart['gitName'].append('CryptoShield')
    newPart['eagleBoard'].append('/Hardware/cryptoshield.brd')
    newPart['eagleSchem'].append('/Hardware/cryptoshield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

