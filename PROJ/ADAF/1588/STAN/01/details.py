
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1588"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1588"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bluefruit Classic PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bluefruit-Classic-PCBs')
    newPart['gitName'].append('Adafruit-Bluefruit-Classic-PCBs')
    newPart['eagleBoard'].append('/Adafruit EZ-Link Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit EZ-Link Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

