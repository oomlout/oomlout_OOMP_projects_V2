
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11835"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11835"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Gram Piano')
    newPart['gitRepo'].append('https://github.com/sparkfun/Gram_Piano')
    newPart['gitName'].append('Gram_Piano')
    newPart['eagleBoard'].append('/Hardware/Gram Piano.brd')
    newPart['eagleSchem'].append('/Hardware/Gram Piano.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

