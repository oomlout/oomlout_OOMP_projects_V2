
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3357"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3357"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Music Maker FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Music-Maker-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Music-Maker-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit VS1053 Amp FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit VS1053 Amp FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

