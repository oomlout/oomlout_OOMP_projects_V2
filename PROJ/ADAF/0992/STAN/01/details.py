
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0992"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0992"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MPL115A2 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MPL115A2-Breakout-PCB')
    newPart['gitName'].append('Adafruit-MPL115A2-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit MPL115A2 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit MPL115A2 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

