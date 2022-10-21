
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1455"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1455"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TLC59711 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TLC59711-Breakout-PCB')
    newPart['gitName'].append('Adafruit-TLC59711-Breakout-PCB')
    newPart['eagleBoard'].append('/adafruit tlc59711 v1.brd')
    newPart['eagleSchem'].append('/adafruit tlc59711 v1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

