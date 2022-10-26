
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12918"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12918"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MCP4725 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MCP4725_Breakout')
    newPart['gitName'].append('MCP4725_Breakout')
    newPart['eagleBoard'].append('/Hardware/MCP4725_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/MCP4725_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

