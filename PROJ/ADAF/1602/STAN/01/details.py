
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1602"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1602"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CAP1188 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CAP1188-PCB')
    newPart['gitName'].append('Adafruit-CAP1188-PCB')
    newPart['eagleBoard'].append('/Adafruit CAP1188.brd')
    newPart['eagleSchem'].append('/Adafruit CAP1188.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

