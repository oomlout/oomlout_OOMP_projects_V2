
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12847"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12847"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XBee Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/XBee_Shield')
    newPart['gitName'].append('XBee_Shield')
    newPart['eagleBoard'].append('/Hardware/Xbee_shield.brd')
    newPart['eagleSchem'].append('/Hardware/Xbee_shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

