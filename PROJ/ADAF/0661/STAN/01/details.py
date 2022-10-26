
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0661"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0661"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 128x32 SPI OLED breakout board PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-128x32-SPI-OLED-breakout-board-PCB')
    newPart['gitName'].append('Adafruit-128x32-SPI-OLED-breakout-board-PCB')
    newPart['eagleBoard'].append('/Adafruit OLED 128x32 Mono.brd')
    newPart['eagleSchem'].append('/Adafruit OLED 128x32 Mono.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

