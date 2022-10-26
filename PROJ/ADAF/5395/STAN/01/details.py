
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5395"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5395"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit QT Py ESP32 Pico PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-QT-Py-ESP32-Pico-PCB')
    newPart['gitName'].append('Adafruit-QT-Py-ESP32-Pico-PCB')
    newPart['eagleBoard'].append('/Adafruit QT Py ESP32 Pico.brd')
    newPart['eagleSchem'].append('/Adafruit QT Py ESP32 Pico.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

