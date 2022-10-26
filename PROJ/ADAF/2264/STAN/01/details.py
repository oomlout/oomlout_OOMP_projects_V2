
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2264"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FT232H Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FT232H-Breakout-PCB')
    newPart['gitName'].append('Adafruit-FT232H-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit FT232H Original.brd')
    newPart['eagleSchem'].append('/Adafruit FT232H Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

