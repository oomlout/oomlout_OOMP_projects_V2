
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15047"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15047"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Lumini 8x8')
    newPart['gitRepo'].append('https://github.com/sparkfun/Lumini_8x8')
    newPart['gitName'].append('Lumini_8x8')
    newPart['eagleBoard'].append('/Hardware/LuMini_8X8.brd')
    newPart['eagleSchem'].append('/Hardware/LuMini_8X8.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

