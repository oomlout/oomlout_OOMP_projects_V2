
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4899"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4899"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SPI Flash SD Card PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SPI-Flash-SD-Card-PCB')
    newPart['gitName'].append('Adafruit-SPI-Flash-SD-Card-PCB')
    newPart['eagleBoard'].append('/Adafruit SPI Flash SD Card.brd')
    newPart['eagleSchem'].append('/Adafruit SPI Flash SD Card.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

