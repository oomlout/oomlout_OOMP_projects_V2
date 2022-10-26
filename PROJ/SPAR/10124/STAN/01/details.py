
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10124"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10124"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RS 485 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/RS-485_Breakout')
    newPart['gitName'].append('RS-485_Breakout')
    newPart['eagleBoard'].append('/Hardware/RS485_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/RS485_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

