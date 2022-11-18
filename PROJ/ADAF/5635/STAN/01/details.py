
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5635"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SPI Flash Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SPI-Flash-Breakout-PCB')
    newPart['gitName'].append('Adafruit-SPI-Flash-Breakout-PCB')
    newPart['eagleBoard'].append('/SPI Flash Rev E.brd')
    newPart['eagleSchem'].append('/SPI Flash Rev E.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

