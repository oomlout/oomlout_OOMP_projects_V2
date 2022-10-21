
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15143"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15143"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LCD TFT Breakout 1in8 128x160')
    newPart['gitRepo'].append('https://github.com/sparkfun/LCD_TFT_Breakout_1in8_128x160')
    newPart['gitName'].append('LCD_TFT_Breakout_1in8_128x160')
    newPart['eagleBoard'].append('/Hardware/LCD_TFT_Breakout_1in8_128x160.brd')
    newPart['eagleSchem'].append('/Hardware/LCD_TFT_Breakout_1in8_128x160.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

