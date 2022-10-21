
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2267"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2267"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bluefruit LE USB Friend and Sniffer PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bluefruit-LE-USB-Friend-and-Sniffer-PCB')
    newPart['gitName'].append('Adafruit-Bluefruit-LE-USB-Friend-and-Sniffer-PCB')
    newPart['eagleBoard'].append('/Adafrruit Bluefruit LE USB Friend CP2102N.brd')
    newPart['eagleSchem'].append('/Adafrruit Bluefruit LE USB Friend CP2102N.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

