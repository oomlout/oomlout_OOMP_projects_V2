
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3533"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3533"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 0.96 160x80 TFT Display Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-0.96-160x80-TFT-Display-Breakout-PCB')
    newPart['gitName'].append('Adafruit-0.96-160x80-TFT-Display-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit 0.96in 160x80 TFT Display.brd')
    newPart['eagleSchem'].append('/Adafruit 0.96in 160x80 TFT Display.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

