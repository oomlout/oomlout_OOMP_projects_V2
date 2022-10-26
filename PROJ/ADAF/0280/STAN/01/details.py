
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0280"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0280"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit USB DC LiPoly Charger')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-USB-DC-LiPoly-Charger')
    newPart['gitName'].append('Adafruit-USB-DC-LiPoly-Charger')
    newPart['eagleBoard'].append('/Adafruit_MCP7386x.brd')
    newPart['eagleSchem'].append('/Adafruit_MCP7386x.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

