
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5146"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5146"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 24LC32 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-24LC32-PCB')
    newPart['gitName'].append('Adafruit-24LC32-PCB')
    newPart['eagleBoard'].append('/Adafruit 24LC32 I2C EEPROM.brd')
    newPart['eagleSchem'].append('/Adafruit 24LC32 I2C EEPROM.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

