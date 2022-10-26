
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9346"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9346"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MegaShield Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/MegaShield_Kit')
    newPart['gitName'].append('MegaShield_Kit')
    newPart['eagleBoard'].append('/Hardware/Mega_Shield-v13.brd')
    newPart['eagleSchem'].append('/Hardware/Mega_Shield-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

