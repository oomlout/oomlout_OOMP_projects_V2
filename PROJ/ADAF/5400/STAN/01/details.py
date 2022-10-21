
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5400"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5400"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ESP32 Feather V2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ESP32-Feather-V2-PCB')
    newPart['gitName'].append('Adafruit-ESP32-Feather-V2-PCB')
    newPart['eagleBoard'].append('/Adafruit ESP32 Feather V2.brd')
    newPart['eagleSchem'].append('/Adafruit ESP32 Feather V2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

