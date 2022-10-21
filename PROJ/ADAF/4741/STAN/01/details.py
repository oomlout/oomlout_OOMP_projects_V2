
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4741"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4741"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Grayscale 1.5 inch 128x128 OLED PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Grayscale-1.5-inch-128x128-OLED-PCB')
    newPart['gitName'].append('Adafruit-Grayscale-1.5-inch-128x128-OLED-PCB')
    newPart['eagleBoard'].append('/Adafruit Grayscale 1.5-inch 128x128 OLED.brd')
    newPart['eagleSchem'].append('/Adafruit Grayscale 1.5-inch 128x128 OLED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

