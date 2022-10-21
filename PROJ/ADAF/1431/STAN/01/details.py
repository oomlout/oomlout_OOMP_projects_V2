
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1431"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1431"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.5inch Color OLED PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.5inch-Color-OLED-PCB')
    newPart['gitName'].append('Adafruit-1.5inch-Color-OLED-PCB')
    newPart['eagleBoard'].append('/Adafruit_1.5_128x128_RGB_OLED.brd')
    newPart['eagleSchem'].append('/Adafruit_1.5_128x128_RGB_OLED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

