
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1893"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1893"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MPL3115A2 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MPL3115A2-PCB')
    newPart['gitName'].append('Adafruit-MPL3115A2-PCB')
    newPart['eagleBoard'].append('/MPL3115A2_v0.2.brd')
    newPart['eagleSchem'].append('/MPL3115A2_v0.2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

