
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14003"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14003"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('THAT 1646 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/THAT_1646_Breakout')
    newPart['gitName'].append('THAT_1646_Breakout')
    newPart['eagleBoard'].append('/Hardware/THAT_1646_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/THAT_1646_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

