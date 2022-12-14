
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5165"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MCP9601 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MCP9601-PCB')
    newPart['gitName'].append('Adafruit-MCP9601-PCB')
    newPart['eagleBoard'].append('/Adafruit MCP9601.brd')
    newPart['eagleSchem'].append('/Adafruit MCP9601.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

