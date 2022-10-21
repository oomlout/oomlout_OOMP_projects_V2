
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1770"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1770"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('2.8 TFT Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/2.8-TFT-Breakout-PCB')
    newPart['gitName'].append('2.8-TFT-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit 2.8 TFT Breakout v2.brd')
    newPart['eagleSchem'].append('/Adafruit 2.8 TFT Breakout v2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

