
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16791"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16791"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Processor Board SAMD51')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Processor_Board-SAMD51')
    newPart['gitName'].append('MicroMod_Processor_Board-SAMD51')
    newPart['eagleBoard'].append('/Hardware/MicroMod_SAMD51.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_SAMD51.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

