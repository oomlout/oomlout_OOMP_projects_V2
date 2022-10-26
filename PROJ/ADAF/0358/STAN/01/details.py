
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0358"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0358"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.8 Inch TFT Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_1.8_Inch_TFT_Breakout_PCB')
    newPart['gitName'].append('Adafruit_1.8_Inch_TFT_Breakout_PCB')
    newPart['eagleBoard'].append('/jdt1800-bob.brd')
    newPart['eagleSchem'].append('/jdt1800-bob.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

