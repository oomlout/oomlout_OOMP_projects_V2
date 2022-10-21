
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3088"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3088"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LED Backpack FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LED-Backpack-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-LED-Backpack-FeatherWing-PCB')
    newPart['eagleBoard'].append('/16x8 mono LED FeatherWing rev A.brd')
    newPart['eagleSchem'].append('/16x8 mono LED FeatherWing rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

