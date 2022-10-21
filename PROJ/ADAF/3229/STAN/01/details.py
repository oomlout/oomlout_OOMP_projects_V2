
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3229"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3229"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Radio FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Radio-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Radio-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit Radio FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit Radio FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

