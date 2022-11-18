
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14312"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic GPS TitanX1')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_GPS-TitanX1')
    newPart['gitName'].append('Qwiic_GPS-TitanX1')
    newPart['eagleBoard'].append('/Hardware/Qwiic GPS - Titan X1.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic GPS - Titan X1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

