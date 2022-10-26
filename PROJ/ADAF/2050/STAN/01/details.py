
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2050"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2050"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('3.5inch TFT Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/3.5inch-TFT-Breakout-PCB')
    newPart['gitName'].append('3.5inch-TFT-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit 3.5in 480x320.brd')
    newPart['eagleSchem'].append('/Adafruit 3.5in 480x320.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

