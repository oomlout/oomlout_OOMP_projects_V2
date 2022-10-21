
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9695"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9695"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MPR121 Capacitive Touch Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MPR121_Capacitive_Touch_Breakout')
    newPart['gitName'].append('MPR121_Capacitive_Touch_Breakout')
    newPart['eagleBoard'].append('/Hardware/MPR121-Breakout-v13.brd')
    newPart['eagleSchem'].append('/Hardware/MPR121-Breakout-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

