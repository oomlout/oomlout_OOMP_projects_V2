
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16401"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16401"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Artemis Processor')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Artemis_Processor')
    newPart['gitName'].append('MicroMod_Artemis_Processor')
    newPart['eagleBoard'].append('/Hardware/MicroMod-Artemis-ProcessorBoard.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod-Artemis-ProcessorBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

