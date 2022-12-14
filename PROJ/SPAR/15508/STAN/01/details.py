
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15508"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15508"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic MCP9600 Thermocouple')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_MCP9600_Thermocouple')
    newPart['gitName'].append('Qwiic_MCP9600_Thermocouple')
    newPart['eagleBoard'].append('/Hardware/Qwiic_MCP9600.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_MCP9600.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

