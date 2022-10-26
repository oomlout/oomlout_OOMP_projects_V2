
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0292"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0292"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit I2C SPI LCD Backpack PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-I2C-SPI-LCD-Backpack-PCB')
    newPart['gitName'].append('Adafruit-I2C-SPI-LCD-Backpack-PCB')
    newPart['eagleBoard'].append('/i2cspilcdbackpack.brd')
    newPart['eagleSchem'].append('/i2cspilcdbackpack.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

