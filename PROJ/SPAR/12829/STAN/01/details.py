
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12829"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12829"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ISL29125 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ISL29125_Breakout')
    newPart['gitName'].append('ISL29125_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ISL29125_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ISL29125_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

