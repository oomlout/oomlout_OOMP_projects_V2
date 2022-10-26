
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4480"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4480"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM6DS33 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM6DS33-PCB')
    newPart['gitName'].append('Adafruit-LSM6DS33-PCB')
    newPart['eagleBoard'].append('/Adfruit LSM6DS33.brd')
    newPart['eagleSchem'].append('/Adfruit LSM6DS33.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

