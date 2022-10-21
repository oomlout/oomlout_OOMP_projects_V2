
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4494"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4494"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DPS310 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DPS310-PCB')
    newPart['gitName'].append('Adafruit-DPS310-PCB')
    newPart['eagleBoard'].append('/Adafruit DPS310.brd')
    newPart['eagleSchem'].append('/Adafruit DPS310.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

