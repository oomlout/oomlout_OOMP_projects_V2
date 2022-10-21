
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3133"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3133"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Ultimate GPS FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Ultimate-GPS-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Ultimate-GPS-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit Ultimate GPS FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit Ultimate GPS FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

