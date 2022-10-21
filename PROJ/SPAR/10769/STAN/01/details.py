
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10769"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10769"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OBD II UART')
    newPart['gitRepo'].append('https://github.com/sparkfun/OBD-II_UART')
    newPart['gitName'].append('OBD-II_UART')
    newPart['eagleBoard'].append('/Hardware/OBD-II-UART.brd')
    newPart['eagleSchem'].append('/Hardware/OBD-II-UART.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

