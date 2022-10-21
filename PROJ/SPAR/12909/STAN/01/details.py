
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12909"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12909"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MS5803 14BA Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MS5803-14BA_Breakout')
    newPart['gitName'].append('MS5803-14BA_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MS5803-14BA_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MS5803-14BA_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

