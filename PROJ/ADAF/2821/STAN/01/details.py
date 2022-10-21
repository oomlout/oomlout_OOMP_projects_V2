
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2821"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2821"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather ESP8266 HUZZAH PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-ESP8266-HUZZAH-PCB')
    newPart['gitName'].append('Adafruit-Feather-ESP8266-HUZZAH-PCB')
    newPart['eagleBoard'].append('/Adafruit ESP8266 Feather rev E.brd')
    newPart['eagleSchem'].append('/Adafruit ESP8266 Feather rev E.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

