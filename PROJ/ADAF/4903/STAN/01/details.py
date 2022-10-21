
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4903"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4903"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ISO1540 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ISO1540-PCB')
    newPart['gitName'].append('Adafruit-ISO1540-PCB')
    newPart['eagleBoard'].append('/Adafruit ISO1540.brd')
    newPart['eagleSchem'].append('/Adafruit ISO1540.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

