
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9607"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9607"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SM5100B Cellular Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/SM5100B_Cellular_Shield')
    newPart['gitName'].append('SM5100B_Cellular_Shield')
    newPart['eagleBoard'].append('/Hardware/cellular shield-v12.brd')
    newPart['eagleSchem'].append('/Hardware/cellular shield-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

