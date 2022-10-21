
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5323"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5323"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather ESP32 S3 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-ESP32-S3-PCB')
    newPart['gitName'].append('Adafruit-Feather-ESP32-S3-PCB')
    newPart['eagleBoard'].append('/Adafruit ESP32-S3 8MB No PSRAM.brd')
    newPart['eagleSchem'].append('/Adafruit ESP32-S3 8MB No PSRAM.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

