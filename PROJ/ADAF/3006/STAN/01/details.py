
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX98357 I2S Amp Breakout')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX98357-I2S-Amp-Breakout')
    newPart['gitName'].append('Adafruit-MAX98357-I2S-Amp-Breakout')
    newPart['eagleBoard'].append('/Adafruit MAX98357 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit MAX98357 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

