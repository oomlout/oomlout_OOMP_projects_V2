
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12082"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12082"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('AD5330 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/AD5330_Breakout')
    newPart['gitName'].append('AD5330_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_AD5330_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_AD5330_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

