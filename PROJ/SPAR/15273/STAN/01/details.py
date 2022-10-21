
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15273"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15273"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator UV')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_UV')
    newPart['gitName'].append('gator_UV')
    newPart['eagleBoard'].append('/Hardware/gator_UV.brd')
    newPart['eagleSchem'].append('/Hardware/gator_UV.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

