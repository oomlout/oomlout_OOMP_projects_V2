
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13763"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13763"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Si7021 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Si7021_Breakout')
    newPart['gitName'].append('Si7021_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Si7021_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Si7021_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

