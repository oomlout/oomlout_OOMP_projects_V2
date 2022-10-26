
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1697"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1697"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bluefruit LE nRF8001 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bluefruit-LE-nRF8001-PCB')
    newPart['gitName'].append('Adafruit-Bluefruit-LE-nRF8001-PCB')
    newPart['eagleBoard'].append('/Adafruit Bluefruit LE nRF8001 v2.brd')
    newPart['eagleSchem'].append('/Adafruit Bluefruit LE nRF8001 v2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

