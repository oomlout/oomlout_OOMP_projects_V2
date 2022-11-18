
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14264"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic UV Sensor ZOPT220x')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_UV_Sensor-ZOPT220x')
    newPart['gitName'].append('Qwiic_UV_Sensor-ZOPT220x')
    newPart['eagleBoard'].append('/Hardware/Qwiic UV Sensor - ZOPT220x.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic UV Sensor - ZOPT220x.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

