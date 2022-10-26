
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4097"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4097"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ADXL343 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_ADXL343_PCB')
    newPart['gitName'].append('Adafruit_ADXL343_PCB')
    newPart['eagleBoard'].append('/Adafruit ADXL343 STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit ADXL343 STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

