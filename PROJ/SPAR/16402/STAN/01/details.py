
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16402"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16402"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Teensy Processor')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Teensy_Processor')
    newPart['gitName'].append('MicroMod_Teensy_Processor')
    newPart['eagleBoard'].append('/Hardware/MicroMod-Teensy.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod-Teensy.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

