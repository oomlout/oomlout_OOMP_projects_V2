
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1120"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1120"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM303 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM303-PCB')
    newPart['gitName'].append('Adafruit-LSM303-PCB')
    newPart['eagleBoard'].append('/Adafruit_LSM303DLHC.brd')
    newPart['eagleSchem'].append('/Adafruit_LSM303DLHC.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

