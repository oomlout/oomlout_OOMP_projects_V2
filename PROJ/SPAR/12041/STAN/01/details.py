
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12041"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12041"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('AT42QT1010 Capacitive Touch Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/AT42QT1010_Capacitive_Touch_Breakout')
    newPart['gitName'].append('AT42QT1010_Capacitive_Touch_Breakout')
    newPart['eagleBoard'].append('/Hardware/AT42QT1010_Capacitive_Touch_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/AT42QT1010_Capacitive_Touch_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

