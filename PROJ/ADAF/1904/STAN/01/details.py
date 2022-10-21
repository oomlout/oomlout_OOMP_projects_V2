
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1904"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1904"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MicroLipo PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MicroLipo-PCB')
    newPart['gitName'].append('Adafruit-MicroLipo-PCB')
    newPart['eagleBoard'].append('/Adafruit MicroLipo.brd')
    newPart['eagleSchem'].append('/Adafruit MicroLipo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

