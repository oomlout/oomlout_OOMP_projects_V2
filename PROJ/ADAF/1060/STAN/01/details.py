
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1060"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1060"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora Smart NeoPixel')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-Smart-NeoPixel')
    newPart['gitName'].append('Adafruit-Flora-Smart-NeoPixel')
    newPart['eagleBoard'].append('/adafruit flora neopixel.brd')
    newPart['eagleSchem'].append('/adafruit flora neopixel.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

