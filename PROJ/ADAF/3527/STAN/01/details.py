
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3527"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3527"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiOLED 128x32 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiOLED-128x32-PCB')
    newPart['gitName'].append('Adafruit-PiOLED-128x32-PCB')
    newPart['eagleBoard'].append('/Adafruit 128x32 Pi OLED.brd')
    newPart['eagleSchem'].append('/Adafruit 128x32 Pi OLED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

