
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2651"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2651"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BMP280 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BMP280-Breakout-PCB')
    newPart['gitName'].append('Adafruit-BMP280-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit BMP280 STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit BMP280 STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

