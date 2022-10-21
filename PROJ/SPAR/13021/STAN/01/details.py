
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13021"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13021"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MagJack Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MagJack_Breakout')
    newPart['gitName'].append('MagJack_Breakout')
    newPart['eagleBoard'].append('/Hardware/MagJack_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/MagJack_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

