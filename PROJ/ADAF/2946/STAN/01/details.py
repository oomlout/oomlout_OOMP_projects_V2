
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2946"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2946"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit IS31FL3731 CharliePlex LED Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-IS31FL3731-CharliePlex-LED-Breakout-PCB')
    newPart['gitName'].append('Adafruit-IS31FL3731-CharliePlex-LED-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit IS31FL3731 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit IS31FL3731 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

