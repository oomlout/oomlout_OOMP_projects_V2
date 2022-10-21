
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1754"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1754"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Pi Cobber PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Pi-Cobber-PCBs')
    newPart['gitName'].append('Adafruit-Pi-Cobber-PCBs')
    newPart['eagleBoard'].append('/Adafruit Cobbler Plus.brd')
    newPart['eagleSchem'].append('/Adafruit Cobbler Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

