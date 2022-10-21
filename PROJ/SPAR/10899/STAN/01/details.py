
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10899"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10899"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyTiny LilyTwinkle')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyTiny_LilyTwinkle')
    newPart['gitName'].append('LilyTiny_LilyTwinkle')
    newPart['eagleBoard'].append('/Hardware/LilyTiny.brd')
    newPart['eagleSchem'].append('/Hardware/LilyTiny.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

