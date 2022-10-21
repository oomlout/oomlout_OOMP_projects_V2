
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3885"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3885"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit STEMMA Speaker PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-STEMMA-Speaker-PCB')
    newPart['gitName'].append('Adafruit-STEMMA-Speaker-PCB')
    newPart['eagleBoard'].append('/Adafruit STEMMA Speaker.brd')
    newPart['eagleSchem'].append('/Adafruit STEMMA Speaker.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

