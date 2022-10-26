
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1899"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1899"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit HTU21D Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-HTU21D-Breakout-PCB')
    newPart['gitName'].append('Adafruit-HTU21D-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit HTU21D-F STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit HTU21D-F STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

