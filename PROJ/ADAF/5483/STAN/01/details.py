
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5483"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5483"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ESP32 S3 TFT Feather PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ESP32-S3-TFT-Feather-PCB')
    newPart['gitName'].append('Adafruit-ESP32-S3-TFT-Feather-PCB')
    newPart['eagleBoard'].append('/Adafruit ESP32-S3 TFT Feather.brd')
    newPart['eagleSchem'].append('/Adafruit ESP32-S3 TFT Feather.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

