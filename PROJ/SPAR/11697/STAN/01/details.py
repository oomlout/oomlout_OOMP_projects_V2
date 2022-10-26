
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11697"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11697"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XBee Explorer Dongle')
    newPart['gitRepo'].append('https://github.com/sparkfun/XBee_Explorer_Dongle')
    newPart['gitName'].append('XBee_Explorer_Dongle')
    newPart['eagleBoard'].append('/Hardware/XBee-Explorer-Dongle.brd')
    newPart['eagleSchem'].append('/Hardware/XBee-Explorer-Dongle.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

