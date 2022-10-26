
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3134"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3134"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 7x15 CharliePlex LED FeatherWing')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-7x15-CharliePlex-LED-FeatherWing')
    newPart['gitName'].append('Adafruit-7x15-CharliePlex-LED-FeatherWing')
    newPart['eagleBoard'].append('/Adafruit CharlieWing.brd')
    newPart['eagleSchem'].append('/Adafruit CharlieWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

