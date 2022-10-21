
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4485"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4485"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM6DS33 LIS3MDL PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM6DS33-LIS3MDL-PCB')
    newPart['gitName'].append('Adafruit-LSM6DS33-LIS3MDL-PCB')
    newPart['eagleBoard'].append('/Adafruit LIS3MDL + LSM6DS33.brd')
    newPart['eagleSchem'].append('/Adafruit LIS3MDL + LSM6DS33.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

