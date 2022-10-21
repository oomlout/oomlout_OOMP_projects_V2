
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2471"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2471"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Huzzah ESP8266 Basic Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Huzzah-ESP8266-Basic-Breakout-PCB')
    newPart['gitName'].append('Adafruit-Huzzah-ESP8266-Basic-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit HUZZAH ESP8266 Basic Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit HUZZAH ESP8266 Basic Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

