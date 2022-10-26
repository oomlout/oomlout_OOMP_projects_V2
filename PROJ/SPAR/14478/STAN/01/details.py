
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14478"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14478"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MaKeyMaKey')
    newPart['gitRepo'].append('https://github.com/sparkfun/MaKeyMaKey')
    newPart['gitName'].append('MaKeyMaKey')
    newPart['eagleBoard'].append('/Hardware/makey_makey.brd')
    newPart['eagleSchem'].append('/Hardware/makey_makey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

