
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15005"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15005"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic GPS RTK')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_GPS-RTK')
    newPart['gitName'].append('Qwiic_GPS-RTK')
    newPart['eagleBoard'].append('/Hardware/Qwiic GPS-RTK - ublox NEO-M8P.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic GPS-RTK - ublox NEO-M8P.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

