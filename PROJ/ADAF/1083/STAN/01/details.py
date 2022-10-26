
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1083"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1083"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADS1X15 Breakout Board PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/ADS1X15-Breakout-Board-PCBs')
    newPart['gitName'].append('ADS1X15-Breakout-Board-PCBs')
    newPart['eagleBoard'].append('/Adafruit ADS1015 ADC STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit ADS1015 ADC STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

