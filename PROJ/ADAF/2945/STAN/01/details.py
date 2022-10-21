
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2945"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2945"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoPixel FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoPixel-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-NeoPixel-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoPixel FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit NeoPixel FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

