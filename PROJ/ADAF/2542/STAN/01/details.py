
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2542"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2542"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FONA 808 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FONA-808-Breakout-PCB')
    newPart['gitName'].append('Adafruit-FONA-808-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit SIM808 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit SIM808 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

