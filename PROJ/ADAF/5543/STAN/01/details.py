
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5543"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5543"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM6DS3TR C LIS3MDL PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM6DS3TR-C-LIS3MDL-PCB')
    newPart['gitName'].append('Adafruit-LSM6DS3TR-C-LIS3MDL-PCB')
    newPart['eagleBoard'].append('/LIS3MDL + LSM6DS3 rev A.brd')
    newPart['eagleSchem'].append('/LIS3MDL + LSM6DS3 rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

