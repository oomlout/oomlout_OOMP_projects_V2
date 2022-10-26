
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11058"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11058"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Venus GPS SMA Connector')
    newPart['gitRepo'].append('https://github.com/sparkfun/Venus_GPS_SMA_Connector')
    newPart['gitName'].append('Venus_GPS_SMA_Connector')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Venus_GPS_SMA_Connector.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Venus_GPS_SMA_Connector.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

