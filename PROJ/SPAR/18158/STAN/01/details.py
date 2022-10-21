
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18158"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18158"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard_Plus')
    newPart['gitName'].append('RedBoard_Plus')
    newPart['eagleBoard'].append('/Hardware/RedBoard_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/RedBoard_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

