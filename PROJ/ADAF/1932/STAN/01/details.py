
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1932"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1932"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit RGB Matrix HAT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-RGB-Matrix-HAT-PCB')
    newPart['gitName'].append('Adafruit-RGB-Matrix-HAT-PCB')
    newPart['eagleBoard'].append('/Adafruit RGB Matrix HAT.brd')
    newPart['eagleSchem'].append('/Adafruit RGB Matrix HAT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

