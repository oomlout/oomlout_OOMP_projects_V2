
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4754"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4754"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BNO08x PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BNO08x-PCB')
    newPart['gitName'].append('Adafruit-BNO08x-PCB')
    newPart['eagleBoard'].append('/Adafruit_BNO08x.brd')
    newPart['eagleSchem'].append('/Adafruit_BNO08x.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

