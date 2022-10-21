
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11569"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11569"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Papilio VGA Wing')
    newPart['gitRepo'].append('https://github.com/sparkfun/Papilio_VGA_Wing')
    newPart['gitName'].append('Papilio_VGA_Wing')
    newPart['eagleBoard'].append('/Hardware/Papilio-VGA_Wing.brd')
    newPart['eagleSchem'].append('/Hardware/Papilio-VGA_Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

