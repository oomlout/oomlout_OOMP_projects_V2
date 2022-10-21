
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RJ45 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/RJ45_Breakout')
    newPart['gitName'].append('RJ45_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_RJ45 Breakout v11.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_RJ45 Breakout v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

