
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14606"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14606"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Flexible Grayscale OLED')
    newPart['gitRepo'].append('https://github.com/sparkfun/Flexible_Grayscale_OLED')
    newPart['gitName'].append('Flexible_Grayscale_OLED')
    newPart['eagleBoard'].append('/Hardware/1.81_Grayscale_OLED_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/1.81_Grayscale_OLED_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

