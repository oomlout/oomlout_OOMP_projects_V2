
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1463"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1463"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoPixel Ring')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoPixel-Ring')
    newPart['gitName'].append('Adafruit-NeoPixel-Ring')
    newPart['eagleBoard'].append('/Adafruit NeoPixel Ring 12.brd')
    newPart['eagleSchem'].append('/Adafruit NeoPixel Ring 12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

