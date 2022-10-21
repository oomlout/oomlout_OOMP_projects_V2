
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1377"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1377"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SMT Breakout PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SMT-Breakout-PCBs')
    newPart['gitName'].append('Adafruit-SMT-Breakout-PCBs')
    newPart['eagleBoard'].append('/0.5mm 4-pin.brd')
    newPart['eagleSchem'].append('/0.5mm 4-pin.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

