
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12617"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12617"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Magician Encoder')
    newPart['gitRepo'].append('https://github.com/sparkfun/Magician_Encoder')
    newPart['gitName'].append('Magician_Encoder')
    newPart['eagleBoard'].append('/Hardware/Magician_encoder.brd')
    newPart['eagleSchem'].append('/Hardware/Magician_encoder.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

