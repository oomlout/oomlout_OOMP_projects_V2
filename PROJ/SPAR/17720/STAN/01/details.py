
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17720"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17720"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Processor RP2040')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Processor-RP2040')
    newPart['gitName'].append('MicroMod_Processor-RP2040')
    newPart['eagleBoard'].append('/Hardware/MicroMod-RP2040-ProcessorBoard.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod-RP2040-ProcessorBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

