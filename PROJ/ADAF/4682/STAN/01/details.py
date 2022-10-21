
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4682"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4682"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MicroSD SPI or SDIO card breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MicroSD-SPI-or-SDIO-card-breakout-PCB')
    newPart['gitName'].append('Adafruit-MicroSD-SPI-or-SDIO-card-breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit SDIO microSD.brd')
    newPart['eagleSchem'].append('/Adafruit SDIO microSD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

