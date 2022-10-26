
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10141"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10141"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LS20126 GPS Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LS20126_GPS_Breakout')
    newPart['gitName'].append('LS20126_GPS_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LS20126-Breakout-v11.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LS20126-Breakout-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

