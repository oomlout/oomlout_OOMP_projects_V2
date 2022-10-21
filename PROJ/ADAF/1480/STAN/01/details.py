
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1480"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1480"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 2.2 SPI TFT')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-2.2-SPI-TFT')
    newPart['gitName'].append('Adafruit-2.2-SPI-TFT')
    newPart['eagleBoard'].append('/Adafruit-2.2-SPI-TFT-v0.2.brd')
    newPart['eagleSchem'].append('/Adafruit-2.2-SPI-TFT-v0.2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

