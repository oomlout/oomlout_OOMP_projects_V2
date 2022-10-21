
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4471"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4471"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MCP2221 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MCP2221-PCB')
    newPart['gitName'].append('Adafruit-MCP2221-PCB')
    newPart['eagleBoard'].append('/Adafruit MCP2221.brd')
    newPart['eagleSchem'].append('/Adafruit MCP2221.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

