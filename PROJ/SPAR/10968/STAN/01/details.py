
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10968"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10968"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('NCP1402 5V Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/NCP1402-5V_Breakout')
    newPart['gitName'].append('NCP1402-5V_Breakout')
    newPart['eagleBoard'].append('/Hardware/NCP1402-5V_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/NCP1402-5V_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

