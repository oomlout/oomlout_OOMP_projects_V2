
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3201"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3201"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Ethernet FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Ethernet-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Ethernet-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit Ethernet FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit Ethernet FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

