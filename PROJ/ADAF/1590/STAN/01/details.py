
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1590"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1590"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit RA8875 Breakout Board PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-RA8875-Breakout-Board-PCB')
    newPart['gitName'].append('Adafruit-RA8875-Breakout-Board-PCB')
    newPart['eagleBoard'].append('/Adafruit RA8875 TFT Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit RA8875 TFT Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

