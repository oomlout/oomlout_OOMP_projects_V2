
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4026"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4026"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit STEMMA Soil Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-STEMMA-Soil-Sensor-PCB')
    newPart['gitName'].append('Adafruit-STEMMA-Soil-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit STEMMA Soil Sensor.brd')
    newPart['eagleSchem'].append('/Adafruit STEMMA Soil Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

