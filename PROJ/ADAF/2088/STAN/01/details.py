
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2088"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2088"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.44 TFT Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.44-TFT-Breakout-PCB')
    newPart['gitName'].append('Adafruit-1.44-TFT-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit TFT144 Breakout rev B.brd')
    newPart['eagleSchem'].append('/Adafruit TFT144 Breakout rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

