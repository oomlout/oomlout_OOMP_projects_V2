
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2999"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2999"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ATWINC1500 WiFi Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ATWINC1500-WiFi-Breakout-PCB')
    newPart['gitName'].append('Adafruit-ATWINC1500-WiFi-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit WINC1500 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit WINC1500 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

