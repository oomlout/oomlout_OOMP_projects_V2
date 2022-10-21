
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15443"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15443"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard Artemis Nano')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard_Artemis_Nano')
    newPart['gitName'].append('RedBoard_Artemis_Nano')
    newPart['eagleBoard'].append('/Hardware/RedBoard-Artemis-Nano.brd')
    newPart['eagleSchem'].append('/Hardware/RedBoard-Artemis-Nano.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

