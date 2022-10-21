
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10570"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10570"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('DangerShield')
    newPart['gitRepo'].append('https://github.com/sparkfun/DangerShield')
    newPart['gitName'].append('DangerShield')
    newPart['eagleBoard'].append('/Hardware/Danger_Shield-v17.brd')
    newPart['eagleSchem'].append('/Hardware/Danger_Shield-v17.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

