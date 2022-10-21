
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10920"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10920"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Venus GPS Logger SMA')
    newPart['gitRepo'].append('https://github.com/sparkfun/Venus_GPS_Logger_SMA')
    newPart['gitName'].append('Venus_GPS_Logger_SMA')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Venus_GPS_Logger.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Venus_GPS_Logger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

