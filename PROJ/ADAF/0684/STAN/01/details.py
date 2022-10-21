
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0684"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0684"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 96x64 RGB OLED Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-96x64-RGB-OLED-Breakout-PCB')
    newPart['gitName'].append('Adafruit-96x64-RGB-OLED-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit 96x64 RGB OLED Breakout v2.0.brd')
    newPart['eagleSchem'].append('/Adafruit 96x64 RGB OLED Breakout v2.0.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

