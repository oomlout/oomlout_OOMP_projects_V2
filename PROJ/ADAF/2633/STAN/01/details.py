
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2633"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2633"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bluefruit LE SPI Friend PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bluefruit-LE-SPI-Friend-PCB')
    newPart['gitName'].append('Adafruit-Bluefruit-LE-SPI-Friend-PCB')
    newPart['eagleBoard'].append('/Adafruit Bluefruit LE SPI Friend.brd')
    newPart['eagleSchem'].append('/Adafruit Bluefruit LE SPI Friend.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

