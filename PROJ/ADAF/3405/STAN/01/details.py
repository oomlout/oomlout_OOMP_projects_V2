
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3405"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3405"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit HUZZAH32 ESP32 Feather PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-HUZZAH32-ESP32-Feather-PCB')
    newPart['gitName'].append('Adafruit-HUZZAH32-ESP32-Feather-PCB')
    newPart['eagleBoard'].append('/Adafruit HUZZAH32 ESP32 Feather.brd')
    newPart['eagleSchem'].append('/Adafruit HUZZAH32 ESP32 Feather.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

