
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14811"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14811"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('A111 Pulsed Radar Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/A111_Pulsed_Radar_Breakout')
    newPart['gitName'].append('A111_Pulsed_Radar_Breakout')
    newPart['eagleBoard'].append('/Hardware/A111_Pulsed_Radar_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/A111_Pulsed_Radar_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

