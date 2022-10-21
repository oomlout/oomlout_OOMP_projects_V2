
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3251"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3251"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Si7021 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Si7021-PCB')
    newPart['gitName'].append('Adafruit-Si7021-PCB')
    newPart['eagleBoard'].append('/Adafruit Si7021 Original.brd')
    newPart['eagleSchem'].append('/Adafruit Si7021 Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

