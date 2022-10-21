
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3677"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3677"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ItsyBitsy 32u4 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ItsyBitsy-32u4-PCB')
    newPart['gitName'].append('Adafruit-ItsyBitsy-32u4-PCB')
    newPart['eagleBoard'].append('/Itsy Bitsy 32u4 3V.brd')
    newPart['eagleSchem'].append('/Itsy Bitsy 32u4 3V.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

