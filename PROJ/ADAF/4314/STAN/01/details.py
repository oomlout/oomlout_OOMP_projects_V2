
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4314"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4314"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ATECC608 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ATECC608-PCB')
    newPart['gitName'].append('Adafruit-ATECC608-PCB')
    newPart['eagleBoard'].append('/Adafruit ATECC608.brd')
    newPart['eagleSchem'].append('/Adafruit ATECC608.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

