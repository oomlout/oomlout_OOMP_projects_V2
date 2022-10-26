
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5632"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5632"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit QSPI DIP Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-QSPI-DIP-Breakout-PCB')
    newPart['gitName'].append('Adafruit-QSPI-DIP-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit QSPI DIP Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit QSPI DIP Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

