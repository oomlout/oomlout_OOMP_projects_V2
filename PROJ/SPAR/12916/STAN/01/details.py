
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12916"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12916"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('HMC6343 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/HMC6343_Breakout')
    newPart['gitName'].append('HMC6343_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_HMC6343_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_HMC6343_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

