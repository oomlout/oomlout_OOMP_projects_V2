
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9614"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9614"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB microB Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_microB_Breakout_Board')
    newPart['gitName'].append('USB_microB_Breakout_Board')
    newPart['eagleBoard'].append('/Hardware/Breakout Board for USB microB.brd')
    newPart['eagleSchem'].append('/Hardware/Breakout Board for USB microB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

