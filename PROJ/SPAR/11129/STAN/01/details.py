
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11129"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11129"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Si4707 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Si4707_Breakout')
    newPart['gitName'].append('Si4707_Breakout')
    newPart['eagleBoard'].append('/hardware/SparkFun_Si4707_Breakout.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_Si4707_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

