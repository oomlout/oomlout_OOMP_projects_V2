
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2487"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2487"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora Bluefruit LE PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-Bluefruit-LE-PCB')
    newPart['gitName'].append('Adafruit-Flora-Bluefruit-LE-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora BLE Friend.brd')
    newPart['eagleSchem'].append('/Adafruit Flora BLE Friend.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

