
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11197"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11197"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ATmega128RFA1 Dev')
    newPart['gitRepo'].append('https://github.com/sparkfun/ATmega128RFA1_Dev')
    newPart['gitName'].append('ATmega128RFA1_Dev')
    newPart['eagleBoard'].append('/hardware/ATmega128RFA1-DevBoard.brd')
    newPart['eagleSchem'].append('/hardware/ATmega128RFA1-DevBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

