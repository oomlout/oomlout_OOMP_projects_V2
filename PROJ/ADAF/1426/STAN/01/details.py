
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1426"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1426"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('NeoPixel Sticks')
    newPart['gitRepo'].append('https://github.com/adafruit/NeoPixel-Sticks')
    newPart['gitName'].append('NeoPixel-Sticks')
    newPart['eagleBoard'].append('/Adafruit NeoPixel 8 Stick v2.brd')
    newPart['eagleSchem'].append('/Adafruit NeoPixel 8 Stick v2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

