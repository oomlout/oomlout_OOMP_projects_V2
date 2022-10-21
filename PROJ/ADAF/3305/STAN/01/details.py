
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3305"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3305"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 50pin to 40pin TFT with AR1100 Adapter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-50pin-to-40pin-TFT-with-AR1100-Adapter-PCB')
    newPart['gitName'].append('Adafruit-50pin-to-40pin-TFT-with-AR1100-Adapter-PCB')
    newPart['eagleBoard'].append('/Adafruit 50pin to 40pin TFT with AR1100 Adapter.brd')
    newPart['eagleSchem'].append('/Adafruit 50pin to 40pin TFT with AR1100 Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

