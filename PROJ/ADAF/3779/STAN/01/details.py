
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3779"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3779"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AS7262 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AS7262-Breakout-PCB')
    newPart['gitName'].append('Adafruit-AS7262-Breakout-PCB')
    newPart['eagleBoard'].append('/AS726x-Spectral_REV-D.brd')
    newPart['eagleSchem'].append('/AS726x-Spectral_REV-D.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

