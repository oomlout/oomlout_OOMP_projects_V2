
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1272"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1272"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit GPS Logger Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-GPS-Logger-Shield-PCB')
    newPart['gitName'].append('Adafruit-GPS-Logger-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit GPS Logger Shield.brd')
    newPart['eagleSchem'].append('/Adafruit GPS Logger Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

