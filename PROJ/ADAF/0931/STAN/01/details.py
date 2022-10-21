
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0931"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0931"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 128x32 I2C OLED Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-128x32-I2C-OLED-Breakout-PCB')
    newPart['gitName'].append('Adafruit-128x32-I2C-OLED-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit OLED 128x32 Mono I2C STEMMA QT rev B.brd')
    newPart['eagleSchem'].append('/Adafruit OLED 128x32 Mono I2C STEMMA QT rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

