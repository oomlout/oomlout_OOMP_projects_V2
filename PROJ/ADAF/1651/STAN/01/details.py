
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1651"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1651"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 2.8 TFT Shield v2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-2.8-TFT-Shield-v2-PCB')
    newPart['gitName'].append('Adafruit-2.8-TFT-Shield-v2-PCB')
    newPart['eagleBoard'].append('/Adafruit tftcaptouchshield rev C.brd')
    newPart['eagleSchem'].append('/Adafruit tftcaptouchshield rev C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

