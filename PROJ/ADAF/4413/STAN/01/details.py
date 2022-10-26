
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4413"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4413"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM303AGR PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM303AGR-PCB')
    newPart['gitName'].append('Adafruit-LSM303AGR-PCB')
    newPart['eagleBoard'].append('/Adafruit_LSM303AGR.brd')
    newPart['eagleSchem'].append('/Adafruit_LSM303AGR.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

