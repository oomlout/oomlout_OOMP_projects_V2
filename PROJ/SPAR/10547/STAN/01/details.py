
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10547"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10547"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Simon Says')
    newPart['gitRepo'].append('https://github.com/sparkfun/Simon-Says')
    newPart['gitName'].append('Simon-Says')
    newPart['eagleBoard'].append('/Hardware/Simon-PTH.brd')
    newPart['eagleSchem'].append('/Hardware/Simon-PTH.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

