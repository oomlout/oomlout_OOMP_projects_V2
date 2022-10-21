
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13598"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13598"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon Proto Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_Proto_Shield')
    newPart['gitName'].append('Photon_Proto_Shield')
    newPart['eagleBoard'].append('/Hardware/Photon_Proto_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Photon_Proto_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

