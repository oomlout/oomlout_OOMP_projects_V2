
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0935"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0935"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MCP4725 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MCP4725-PCB')
    newPart['gitName'].append('Adafruit-MCP4725-PCB')
    newPart['eagleBoard'].append('/Adafruit MCP4725 Original.brd')
    newPart['eagleSchem'].append('/Adafruit MCP4725 Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

