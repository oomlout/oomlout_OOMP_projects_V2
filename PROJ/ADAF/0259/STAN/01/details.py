
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0259"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0259"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MCP73833 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_MCP73833_PCB')
    newPart['gitName'].append('Adafruit_MCP73833_PCB')
    newPart['eagleBoard'].append('/MCP73833_QFN_v1.0.brd')
    newPart['eagleSchem'].append('/MCP73833_QFN_v1.0.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

