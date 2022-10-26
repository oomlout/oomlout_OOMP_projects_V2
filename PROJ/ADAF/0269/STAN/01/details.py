
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0269"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0269"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX31855 breakout board')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX31855-breakout-board')
    newPart['gitName'].append('Adafruit-MAX31855-breakout-board')
    newPart['eagleBoard'].append('/Adafruit_MAX31855 v2.brd')
    newPart['eagleSchem'].append('/Adafruit_MAX31855 v2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

