
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9981"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9981"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SC16IS750 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SC16IS750_Breakout')
    newPart['gitName'].append('SC16IS750_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_SC16IS750_Breakout-v13.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_SC16IS750_Breakout-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

