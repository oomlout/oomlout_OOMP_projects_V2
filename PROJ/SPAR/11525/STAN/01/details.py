
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11525"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11525"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('P8X32A Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/P8X32A_Breakout')
    newPart['gitName'].append('P8X32A_Breakout')
    newPart['eagleBoard'].append('/hardware/P8X32A_Breakout.brd')
    newPart['eagleSchem'].append('/hardware/P8X32A_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

