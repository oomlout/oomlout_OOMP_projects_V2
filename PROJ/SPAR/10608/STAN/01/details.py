
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10608"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10608"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MP3 Breakout VS1033D')
    newPart['gitRepo'].append('https://github.com/sparkfun/MP3_Breakout-VS1033D')
    newPart['gitName'].append('MP3_Breakout-VS1033D')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MP3_Breakout-VS1033D.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MP3_Breakout-VS1033D.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

