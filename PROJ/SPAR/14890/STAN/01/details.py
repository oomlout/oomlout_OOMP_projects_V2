
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14890"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14890"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator color')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_color')
    newPart['gitName'].append('gator_color')
    newPart['eagleBoard'].append('/Hardware/gatorBytes_LED_board.brd')
    newPart['eagleSchem'].append('/Hardware/gatorBytes_LED_board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

