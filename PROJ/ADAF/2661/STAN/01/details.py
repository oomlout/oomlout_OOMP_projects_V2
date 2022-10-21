
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2661"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2661"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bluefruit LE Micro PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bluefruit-LE-Micro-PCB')
    newPart['gitName'].append('Adafruit-Bluefruit-LE-Micro-PCB')
    newPart['eagleBoard'].append('/Adafruit Bluefruit LE Micro Rev B.brd')
    newPart['eagleSchem'].append('/Adafruit Bluefruit LE Micro Rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

