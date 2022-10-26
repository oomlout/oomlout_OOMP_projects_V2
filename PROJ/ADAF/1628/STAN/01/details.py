
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1628"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1628"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bluefruit EZ Link Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bluefruit-EZ-Link-Shield-PCB')
    newPart['gitName'].append('Adafruit-Bluefruit-EZ-Link-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit EZ-Link Shield.brd')
    newPart['eagleSchem'].append('/Adafruit EZ-Link Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

