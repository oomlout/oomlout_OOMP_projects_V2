
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19626"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19626"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('8 channel level shifter TXS0108E')
    newPart['gitRepo'].append('https://github.com/sparkfun/8_channel_level_shifter_TXS0108E')
    newPart['gitName'].append('8_channel_level_shifter_TXS0108E')
    newPart['eagleBoard'].append('/Hardware/TXS0108 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/TXS0108 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

