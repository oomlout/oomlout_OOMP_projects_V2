
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FemtoBuck')
    newPart['gitRepo'].append('https://github.com/sparkfun/FemtoBuck')
    newPart['gitName'].append('FemtoBuck')
    newPart['eagleBoard'].append('/hardware/femtobuck.brd')
    newPart['eagleSchem'].append('/hardware/femtobuck.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

