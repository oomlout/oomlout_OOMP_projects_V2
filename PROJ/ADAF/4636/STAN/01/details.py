
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4636"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SHTC3 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SHTC3-PCB')
    newPart['gitName'].append('Adafruit-SHTC3-PCB')
    newPart['eagleBoard'].append('/Adafruit_SHTC3.brd')
    newPart['eagleSchem'].append('/Adafruit_SHTC3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

