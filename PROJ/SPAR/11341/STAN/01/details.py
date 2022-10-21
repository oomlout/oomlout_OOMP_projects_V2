
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11341"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11341"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Gyro Breakout LPY503AL')
    newPart['gitRepo'].append('https://github.com/sparkfun/Gyro_Breakout-LPY503AL')
    newPart['gitName'].append('Gyro_Breakout-LPY503AL')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Gyro_Breakout-LPY503AL.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Gyro_Breakout-LPY503AL.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

