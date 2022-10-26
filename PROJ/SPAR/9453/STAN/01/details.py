
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9453"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9453"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QRE1113 Line Sensor Analog')
    newPart['gitRepo'].append('https://github.com/sparkfun/QRE1113_Line_Sensor-Analog')
    newPart['gitName'].append('QRE1113_Line_Sensor-Analog')
    newPart['eagleBoard'].append('/Hardware/QRE1113 Line Sensor Breakout - Analog.brd')
    newPart['eagleSchem'].append('/Hardware/QRE1113 Line Sensor Breakout - Analog.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

