
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5297"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5297"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.12in 128x128 OLED PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.12in-128x128-OLED-PCB')
    newPart['gitName'].append('Adafruit-1.12in-128x128-OLED-PCB')
    newPart['eagleBoard'].append('/Adafruit Monochrome 1.12in 128x128 OLED.brd')
    newPart['eagleSchem'].append('/Adafruit Monochrome 1.12in 128x128 OLED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

