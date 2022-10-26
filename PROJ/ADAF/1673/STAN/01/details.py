
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1673"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1673"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.27inch Color OLED Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.27inch-Color-OLED-Breakout-PCB')
    newPart['gitName'].append('Adafruit-1.27inch-Color-OLED-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit 1.27 128x96 RGB OLED.brd')
    newPart['eagleSchem'].append('/Adafruit 1.27 128x96 RGB OLED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

