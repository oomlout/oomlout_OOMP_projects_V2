
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11043"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11043"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('fabFM Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/fabFM-Kit')
    newPart['gitName'].append('fabFM-Kit')
    newPart['eagleBoard'].append('/hardware/fabfm.brd')
    newPart['eagleSchem'].append('/hardware/fabfm.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

