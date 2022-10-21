
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9322"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9322"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photo Interrupter Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photo_Interrupter_Breakout')
    newPart['gitName'].append('Photo_Interrupter_Breakout')
    newPart['eagleBoard'].append('/Hardware/PhotoInterrupter-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/PhotoInterrupter-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

