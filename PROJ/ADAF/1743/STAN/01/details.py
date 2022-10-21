
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1743"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1743"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 3.2 TFT Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-3.2-TFT-Breakout-PCB')
    newPart['gitName'].append('Adafruit-3.2-TFT-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit 3.2in TFT 320x240.brd')
    newPart['eagleSchem'].append('/Adafruit 3.2in TFT 320x240.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

