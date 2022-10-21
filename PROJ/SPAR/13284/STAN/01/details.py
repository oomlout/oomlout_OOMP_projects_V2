
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13284"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LSM9DS1 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LSM9DS1_Breakout')
    newPart['gitName'].append('LSM9DS1_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun-LSM9DS1-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun-LSM9DS1-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

