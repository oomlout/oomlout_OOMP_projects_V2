
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2923"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2923"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Relay FeatherWing PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Relay-FeatherWing-PCBs')
    newPart['gitName'].append('Adafruit-Relay-FeatherWing-PCBs')
    newPart['eagleBoard'].append('/Adafruit Latching Relay FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit Latching Relay FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

