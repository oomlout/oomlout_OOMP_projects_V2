
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2900"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2900"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit OLED FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-OLED-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-OLED-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit 128x64 OLED FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit 128x64 OLED FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

