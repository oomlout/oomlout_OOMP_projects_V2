
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5233"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5233"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ATtiny8x7 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ATtiny8x7-Breakout-PCB')
    newPart['gitName'].append('Adafruit-ATtiny8x7-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit ATtiny8x7 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit ATtiny8x7 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

