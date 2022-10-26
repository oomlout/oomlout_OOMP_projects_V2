
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2466"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2466"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit METRO 328 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-METRO-328-PCB')
    newPart['gitName'].append('Adafruit-METRO-328-PCB')
    newPart['eagleBoard'].append('/Metro Mini 328 V2 - STEMMA QT.brd')
    newPart['eagleSchem'].append('/Metro Mini 328 V2 - STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

