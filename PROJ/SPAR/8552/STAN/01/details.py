
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8552"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8552"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial DB9 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_DB9_Breakout')
    newPart['gitName'].append('Serial_DB9_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Serial_DB9-Breakout-v13.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Serial_DB9-Breakout-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

