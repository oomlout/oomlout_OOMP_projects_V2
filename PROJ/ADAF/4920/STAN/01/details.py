
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4920"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4920"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TPS62827 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TPS62827-PCB')
    newPart['gitName'].append('Adafruit-TPS62827-PCB')
    newPart['eagleBoard'].append('/TPS62827 3.3V Buck Converter.brd')
    newPart['eagleSchem'].append('/TPS62827 3.3V Buck Converter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

