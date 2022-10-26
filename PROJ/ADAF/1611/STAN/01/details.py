
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1611"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1611"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Trellis')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_Trellis')
    newPart['gitName'].append('Adafruit_Trellis')
    newPart['eagleBoard'].append('/Adafruit Trellis 4x4 3mm HT16K33.brd')
    newPart['eagleSchem'].append('/Adafruit Trellis 4x4 3mm HT16K33.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

