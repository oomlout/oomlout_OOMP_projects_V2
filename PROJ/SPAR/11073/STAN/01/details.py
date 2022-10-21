
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11073"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11073"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GP 2106 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/GP-2106_Breakout')
    newPart['gitName'].append('GP-2106_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GP-2106_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GP-2106_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

