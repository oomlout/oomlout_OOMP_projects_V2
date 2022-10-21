
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1430"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1430"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoPixel Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoPixel-Shield-PCB')
    newPart['gitName'].append('Adafruit-NeoPixel-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoPixel Shield v2.brd')
    newPart['eagleSchem'].append('/Adafruit NeoPixel Shield v2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

