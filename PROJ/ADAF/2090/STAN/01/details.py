
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2090"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2090"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 2.8 TFT with Capacitive Touch PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-2.8-TFT-with-Capacitive-Touch-PCB')
    newPart['gitName'].append('Adafruit-2.8-TFT-with-Capacitive-Touch-PCB')
    newPart['eagleBoard'].append('/Adafruit 2.8 inch TFT w Capacitive Touch.brd')
    newPart['eagleSchem'].append('/Adafruit 2.8 inch TFT w Capacitive Touch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

