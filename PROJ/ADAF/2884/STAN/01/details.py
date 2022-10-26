
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2884"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2884"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FeatherWing Proto Doubler Tripler and Quad')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FeatherWing-Proto-Doubler-Tripler-and-Quad')
    newPart['gitName'].append('Adafruit-FeatherWing-Proto-Doubler-Tripler-and-Quad')
    newPart['eagleBoard'].append('/DoubleWing.brd')
    newPart['eagleSchem'].append('/DoubleWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

