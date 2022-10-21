
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12731"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12731"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FT232RL USB Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/FT232RL_USB_Breakout')
    newPart['gitName'].append('FT232RL_USB_Breakout')
    newPart['eagleBoard'].append('/Hardware/FT232R-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/FT232R-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

