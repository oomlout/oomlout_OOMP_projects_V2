
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11684"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11684"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MP3 Breakout VS1063')
    newPart['gitRepo'].append('https://github.com/sparkfun/MP3_Breakout-VS1063')
    newPart['gitName'].append('MP3_Breakout-VS1063')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MP3_Breakout-VS1063.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MP3_Breakout-VS1063.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

