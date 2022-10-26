
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1312"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Breadboard NeoPixel PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_Breadboard_NeoPixel_PCB')
    newPart['gitName'].append('Adafruit_Breadboard_NeoPixel_PCB')
    newPart['eagleBoard'].append('/Adafruit_Breadboard_NeoPixel.brd')
    newPart['eagleSchem'].append('/Adafruit_Breadboard_NeoPixel.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

