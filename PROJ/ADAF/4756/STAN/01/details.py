
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4756"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4756"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LTC4311 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LTC4311-PCB')
    newPart['gitName'].append('Adafruit-LTC4311-PCB')
    newPart['eagleBoard'].append('/Adafruit LTC4311 I2C Extender.brd')
    newPart['eagleSchem'].append('/Adafruit LTC4311 I2C Extender.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

