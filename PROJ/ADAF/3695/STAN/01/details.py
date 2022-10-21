
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3695"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3695"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DragonTail for micro bit PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DragonTail-for-micro-bit-PCB')
    newPart['gitName'].append('Adafruit-DragonTail-for-micro-bit-PCB')
    newPart['eagleBoard'].append('/Adafruit DragonTail.brd')
    newPart['eagleSchem'].append('/Adafruit DragonTail.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

