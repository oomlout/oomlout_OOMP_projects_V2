
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18573"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18573"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Function LoRa 1W')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Function_LoRa_1W')
    newPart['gitName'].append('MicroMod_Function_LoRa_1W')
    newPart['eagleBoard'].append('/Hardware/MicroMod-LoRa-1W-Function-Board.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod-LoRa-1W-Function-Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

