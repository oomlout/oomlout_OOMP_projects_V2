
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14050"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14050"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial Basic Breakout CH340G')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_Basic_Breakout-CH340G')
    newPart['gitName'].append('Serial_Basic_Breakout-CH340G')
    newPart['eagleBoard'].append('/Hardware/Serial-Basic.brd')
    newPart['eagleSchem'].append('/Hardware/Serial-Basic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

