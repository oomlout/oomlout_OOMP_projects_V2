
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9116"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('DS1077 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/DS1077_Breakout')
    newPart['gitName'].append('DS1077_Breakout')
    newPart['eagleBoard'].append('/Hardware/DS1077_breakout.brd')
    newPart['eagleSchem'].append('/Hardware/DS1077_breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

