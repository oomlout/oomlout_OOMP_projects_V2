
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13743"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13743"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Shifting microSD')
    newPart['gitRepo'].append('https://github.com/sparkfun/Shifting_microSD')
    newPart['gitName'].append('Shifting_microSD')
    newPart['eagleBoard'].append('/Hardware/Shifting_microSD.brd')
    newPart['eagleSchem'].append('/Hardware/Shifting_microSD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

