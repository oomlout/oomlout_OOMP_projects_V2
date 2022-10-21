
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13038"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13038"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison GPIO Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_GPIO_Block')
    newPart['gitName'].append('Edison_GPIO_Block')
    newPart['eagleBoard'].append('/Hardware/GPIO_Block.brd')
    newPart['eagleSchem'].append('/Hardware/GPIO_Block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

