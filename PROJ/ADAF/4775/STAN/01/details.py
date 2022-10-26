
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4775"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4775"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Metro ESP32 S2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Metro-ESP32-S2-PCB')
    newPart['gitName'].append('Adafruit-Metro-ESP32-S2-PCB')
    newPart['eagleBoard'].append('/Adafruit Metro ESP32-S2.brd')
    newPart['eagleSchem'].append('/Adafruit Metro ESP32-S2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

