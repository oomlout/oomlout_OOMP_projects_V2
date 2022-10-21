
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13036"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13036"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison Arduino Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_Arduino_Block')
    newPart['gitName'].append('Edison_Arduino_Block')
    newPart['eagleBoard'].append('/Hardware/arduino_block.brd')
    newPart['eagleSchem'].append('/Hardware/arduino_block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

