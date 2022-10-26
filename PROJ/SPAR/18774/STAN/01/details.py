
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18774"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18774"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun GNSS Timing ZED F9T')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_GNSS_Timing-ZED-F9T')
    newPart['gitName'].append('SparkFun_GNSS_Timing-ZED-F9T')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GNSS_Timing-ZED-F9T.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GNSS_Timing-ZED-F9T.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

