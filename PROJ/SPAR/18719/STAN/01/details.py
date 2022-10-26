
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18719"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18719"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun GNSS Dead Reckoning ZED F9K')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_GNSS_Dead_Reckoning_ZED-F9K')
    newPart['gitName'].append('SparkFun_GNSS_Dead_Reckoning_ZED-F9K')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GPS_ZED-F9K.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GPS_ZED-F9K.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

