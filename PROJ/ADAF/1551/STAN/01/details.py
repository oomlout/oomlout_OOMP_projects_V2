
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1551"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1551"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DS2413 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DS2413-PCB')
    newPart['gitName'].append('Adafruit-DS2413-PCB')
    newPart['eagleBoard'].append('/Adafruit DS2413.brd')
    newPart['eagleSchem'].append('/Adafruit DS2413.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

