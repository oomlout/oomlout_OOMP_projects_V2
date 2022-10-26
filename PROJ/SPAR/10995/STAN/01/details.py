
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10995"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10995"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GPS Evaluation Board GP 2106')
    newPart['gitRepo'].append('https://github.com/sparkfun/GPS_Evaluation_Board_GP-2106')
    newPart['gitName'].append('GPS_Evaluation_Board_GP-2106')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GPS_Evaluation_Board_GP-2106.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GPS_Evaluation_Board_GP-2106.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

