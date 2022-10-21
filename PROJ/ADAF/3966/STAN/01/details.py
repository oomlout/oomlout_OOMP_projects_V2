
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3966"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3966"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BMP3xx PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BMP3xx-PCB')
    newPart['gitName'].append('Adafruit-BMP3xx-PCB')
    newPart['eagleBoard'].append('/Adafruit BMP388 QT.brd')
    newPart['eagleSchem'].append('/Adafruit BMP388 QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

