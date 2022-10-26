
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5631"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PB86 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PB86-Breakout-PCB')
    newPart['gitName'].append('Adafruit-PB86-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit PB86 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit PB86 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

