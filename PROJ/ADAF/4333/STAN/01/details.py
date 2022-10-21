
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4333"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4333"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Circuit Playground Bluefruit PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Circuit-Playground-Bluefruit-PCB')
    newPart['gitName'].append('Adafruit-Circuit-Playground-Bluefruit-PCB')
    newPart['eagleBoard'].append('/Adafruit Circuit Playground Bluefruit.brd')
    newPart['eagleSchem'].append('/Adafruit Circuit Playground Bluefruit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

