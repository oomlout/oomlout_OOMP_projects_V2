
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14414"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14414"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun GPS Breakout XA1110 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_GPS_Breakout_XA1110_Qwiic')
    newPart['gitName'].append('SparkFun_GPS_Breakout_XA1110_Qwiic')
    newPart['eagleBoard'].append('/Hardware/Qwiic GPS - Titan X1.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic GPS - Titan X1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

