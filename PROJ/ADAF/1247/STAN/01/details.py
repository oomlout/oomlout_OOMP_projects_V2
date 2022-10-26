
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1247"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1247"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora LSM303 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-LSM303-PCB')
    newPart['gitName'].append('Adafruit-Flora-LSM303-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora LSM303.brd')
    newPart['eagleSchem'].append('/Adafruit Flora LSM303.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

