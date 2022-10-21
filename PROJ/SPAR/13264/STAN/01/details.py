
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13264"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPixel')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPixel')
    newPart['gitName'].append('LilyPixel')
    newPart['eagleBoard'].append('/Hardware/SparkFunLilyPixel.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFunLilyPixel.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

