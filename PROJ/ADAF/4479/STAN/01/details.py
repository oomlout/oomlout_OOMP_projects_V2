
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4479"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4479"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LIS3MDL PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LIS3MDL-PCB')
    newPart['gitName'].append('Adafruit-LIS3MDL-PCB')
    newPart['eagleBoard'].append('/Adafruit LIS3MDL.brd')
    newPart['eagleSchem'].append('/Adafruit LIS3MDL.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

