
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3191"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3191"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Power Relay FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Power-Relay-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Power-Relay-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit PowerRelay Wing.brd')
    newPart['eagleSchem'].append('/Adafruit PowerRelay Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

