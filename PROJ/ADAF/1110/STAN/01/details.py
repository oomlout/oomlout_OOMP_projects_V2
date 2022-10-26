
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1110"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1110"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 16x2 LCD Pi Plate')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-16x2-LCD-Pi-Plate')
    newPart['gitName'].append('Adafruit-16x2-LCD-Pi-Plate')
    newPart['eagleBoard'].append('/adafruit_rgblcdplate.brd')
    newPart['eagleSchem'].append('/adafruit_rgblcdplate.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

