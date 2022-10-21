
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1603"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1603"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BMP180 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BMP180-PCB')
    newPart['gitName'].append('Adafruit-BMP180-PCB')
    newPart['eagleBoard'].append('/Adafruit BMP180.brd')
    newPart['eagleSchem'].append('/Adafruit BMP180.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

