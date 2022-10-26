
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0390"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0390"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB DC Solar Lithium Ion Polymer charger')
    newPart['gitRepo'].append('https://github.com/adafruit/USB-DC-Solar-Lithium-Ion-Polymer-charger')
    newPart['gitName'].append('USB-DC-Solar-Lithium-Ion-Polymer-charger')
    newPart['eagleBoard'].append('/Adafruit MCP73871 Solar Charger v4.brd')
    newPart['eagleSchem'].append('/Adafruit MCP73871 Solar Charger v4.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

