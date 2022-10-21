
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather ESP32 S2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-ESP32-S2-PCB')
    newPart['gitName'].append('Adafruit-Feather-ESP32-S2-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather ESP32-S2 Rev C.brd')
    newPart['eagleSchem'].append('/Adafruit Feather ESP32-S2 Rev C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

