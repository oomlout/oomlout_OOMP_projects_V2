
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16475"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16475"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun GPS Dead Reckoning PHat ZED F9R')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_GPS_Dead_Reckoning_PHat_ZED-F9R')
    newPart['gitName'].append('SparkFun_GPS_Dead_Reckoning_PHat_ZED-F9R')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GPS_ZED-F9R_pHat.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GPS_ZED-F9R_pHat.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

