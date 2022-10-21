
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4172"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4172"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ESP32 HUZZAH Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ESP32-HUZZAH-Breakout-PCB')
    newPart['gitName'].append('Adafruit-ESP32-HUZZAH-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit ESP32 Huzzah Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit ESP32 Huzzah Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

