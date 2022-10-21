
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9546"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9546"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XMega100 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/XMega100_Breakout')
    newPart['gitName'].append('XMega100_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_XMega100_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_XMega100_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

