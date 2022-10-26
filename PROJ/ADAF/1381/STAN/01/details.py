
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1381"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1381"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VS1053 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VS1053-Breakout-PCB')
    newPart['gitName'].append('Adafruit-VS1053-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit VS1053 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit VS1053 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

