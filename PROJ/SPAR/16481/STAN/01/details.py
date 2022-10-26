
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16481"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16481"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic GPS RTK2')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_GPS-RTK2')
    newPart['gitName'].append('Qwiic_GPS-RTK2')
    newPart['eagleBoard'].append('/Hardware/Qwiic GPS-RTK2 - ublox ZED-F9P.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic GPS-RTK2 - ublox ZED-F9P.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

