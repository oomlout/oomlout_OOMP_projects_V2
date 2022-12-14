
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3317"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3317"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VL53L0X ToF Distance Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VL53L0X-ToF-Distance-Sensor-PCB')
    newPart['gitName'].append('Adafruit-VL53L0X-ToF-Distance-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit VL530X STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit VL530X STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

