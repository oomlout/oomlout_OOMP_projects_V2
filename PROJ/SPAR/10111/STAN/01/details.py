
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10111"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10111"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Tri Color Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Tri-Color_Breakout')
    newPart['gitName'].append('Tri-Color_Breakout')
    newPart['eagleBoard'].append('/Hardware/Tri-color LED Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Tri-color LED Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

