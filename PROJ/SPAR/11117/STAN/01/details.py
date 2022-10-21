
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11117"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11117"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('32U4 Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/32U4_Breakout_Board')
    newPart['gitName'].append('32U4_Breakout_Board')
    newPart['eagleBoard'].append('/Hardware/32U4_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/32U4_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

