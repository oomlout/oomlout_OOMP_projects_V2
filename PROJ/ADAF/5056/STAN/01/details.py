
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5056"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5056"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Trinkey QT2040 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Trinkey-QT2040-PCB')
    newPart['gitName'].append('Adafruit-Trinkey-QT2040-PCB')
    newPart['eagleBoard'].append('/Adafruit QT2040 Trinkey.brd')
    newPart['eagleSchem'].append('/Adafruit QT2040 Trinkey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

