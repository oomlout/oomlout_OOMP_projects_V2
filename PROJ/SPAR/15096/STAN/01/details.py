
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15096"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15096"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial Basic Breakout CH340C')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_Basic_Breakout-CH340C')
    newPart['gitName'].append('Serial_Basic_Breakout-CH340C')
    newPart['eagleBoard'].append('/Hardware/Serial-Basic-CH340C.brd')
    newPart['eagleSchem'].append('/Hardware/Serial-Basic-CH340C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

