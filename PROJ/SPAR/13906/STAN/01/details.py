
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13906"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13906"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('74HC4051 8 Channel Mux Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/74HC4051_8-Channel_Mux_Breakout')
    newPart['gitName'].append('74HC4051_8-Channel_Mux_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun-74HC4051-8-Channel-Mux-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun-74HC4051-8-Channel-Mux-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

