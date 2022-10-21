
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10467"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10467"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LED Tactile Button Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LED_Tactile_Button_Breakout')
    newPart['gitName'].append('LED_Tactile_Button_Breakout')
    newPart['eagleBoard'].append('/Hardware/Button-LED-Breakout-v10.brd')
    newPart['eagleSchem'].append('/Hardware/Button-LED-Breakout-v10.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

