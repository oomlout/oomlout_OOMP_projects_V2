
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11818"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11818"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GPS Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/GPS_Breakout')
    newPart['gitName'].append('GPS_Breakout')
    newPart['eagleBoard'].append('/Hardware/GPS_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/GPS_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

