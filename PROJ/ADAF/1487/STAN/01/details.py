
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1487"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1487"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoPixel 8x8 Matrix')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoPixel-8x8-Matrix')
    newPart['gitName'].append('Adafruit-NeoPixel-8x8-Matrix')
    newPart['eagleBoard'].append('/Adafruit_NeoMatrix_8x8 v2.brd')
    newPart['eagleSchem'].append('/Adafruit_NeoMatrix_8x8 v2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

