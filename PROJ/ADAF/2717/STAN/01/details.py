
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2717"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2717"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TCA9548A I2C Multiplexer PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TCA9548A-I2C-Multiplexer-PCB')
    newPart['gitName'].append('Adafruit-TCA9548A-I2C-Multiplexer-PCB')
    newPart['eagleBoard'].append('/Adafruit TCA9548A.brd')
    newPart['eagleSchem'].append('/Adafruit TCA9548A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

