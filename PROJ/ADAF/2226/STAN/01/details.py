
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2226"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2226"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoPixel Jewel 7')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoPixel-Jewel-7')
    newPart['gitName'].append('Adafruit-NeoPixel-Jewel-7')
    newPart['eagleBoard'].append('/Adafruit NeoJewel 7.brd')
    newPart['eagleSchem'].append('/Adafruit NeoJewel 7.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

