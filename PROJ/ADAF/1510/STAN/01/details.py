
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1510"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1510"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CC3000 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CC3000-Breakout-PCB')
    newPart['gitName'].append('Adafruit-CC3000-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit CC3000 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit CC3000 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

