
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3967"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3967"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VL53L1X PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VL53L1X-PCB')
    newPart['gitName'].append('Adafruit-VL53L1X-PCB')
    newPart['eagleBoard'].append('/Adafruit VL53L1X.brd')
    newPart['eagleSchem'].append('/Adafruit VL53L1X.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

