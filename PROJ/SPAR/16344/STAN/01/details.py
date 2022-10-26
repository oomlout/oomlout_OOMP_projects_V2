
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16344"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16344"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun GPS Dead Reckoning ZED F9R')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_GPS_Dead_Reckoning_ZED-F9R')
    newPart['gitName'].append('SparkFun_GPS_Dead_Reckoning_ZED-F9R')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GPS_ZED-F9R_BoB.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GPS_ZED-F9R_BoB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

