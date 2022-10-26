
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4470"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4470"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MCP4728 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MCP4728-PCB')
    newPart['gitName'].append('Adafruit-MCP4728-PCB')
    newPart['eagleBoard'].append('/Adafruit MCP4728.brd')
    newPart['eagleSchem'].append('/Adafruit MCP4728.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

