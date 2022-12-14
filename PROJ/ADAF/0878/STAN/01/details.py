
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0878"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0878"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LED Backpacks')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LED-Backpacks')
    newPart['gitName'].append('Adafruit-LED-Backpacks')
    newPart['eagleBoard'].append('/Adafruit 0.54 Alphanumeric STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit 0.54 Alphanumeric STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

