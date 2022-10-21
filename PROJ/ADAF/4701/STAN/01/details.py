
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4701"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4701"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ST25DV16 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ST25DV16-PCB')
    newPart['gitName'].append('Adafruit-ST25DV16-PCB')
    newPart['eagleBoard'].append('/Adafruit ST25DV16.brd')
    newPart['eagleSchem'].append('/Adafruit ST25DV16.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

