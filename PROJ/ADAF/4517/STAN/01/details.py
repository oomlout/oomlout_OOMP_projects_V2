
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4517"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4517"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM6DSOX LIS3MDL PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM6DSOX-LIS3MDL-PCB')
    newPart['gitName'].append('Adafruit-LSM6DSOX-LIS3MDL-PCB')
    newPart['eagleBoard'].append('/Adafruit LIS3MDL + LSM6DSOX FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit LIS3MDL + LSM6DSOX FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

