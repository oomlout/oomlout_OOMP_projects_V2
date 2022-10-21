
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4808"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4808"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit EMC2101 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-EMC2101-PCB')
    newPart['gitName'].append('Adafruit-EMC2101-PCB')
    newPart['eagleBoard'].append('/Adafruit_EMC2101.brd')
    newPart['eagleSchem'].append('/Adafruit_EMC2101.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

