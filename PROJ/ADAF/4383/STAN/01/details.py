
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4383"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4383"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.14 inch 240x135 TFT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.14-inch-240x135-TFT-PCB')
    newPart['gitName'].append('Adafruit-1.14-inch-240x135-TFT-PCB')
    newPart['eagleBoard'].append('/Adafruit 1.14-inch 240x135 Color TFT.brd')
    newPart['eagleSchem'].append('/Adafruit 1.14-inch 240x135 Color TFT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

