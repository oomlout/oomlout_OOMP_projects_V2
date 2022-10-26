
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2045"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2045"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Si5351A Clock Generator Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Si5351A-Clock-Generator-Breakout-PCB')
    newPart['gitName'].append('Adafruit-Si5351A-Clock-Generator-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit Si5351A.brd')
    newPart['eagleSchem'].append('/Adafruit Si5351A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

