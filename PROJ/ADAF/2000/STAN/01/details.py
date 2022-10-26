
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Pro Trinket PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Pro-Trinket-PCBs')
    newPart['gitName'].append('Adafruit-Pro-Trinket-PCBs')
    newPart['eagleBoard'].append('/Adafruit Pro Trinket 3v3.brd')
    newPart['eagleSchem'].append('/Adafruit Pro Trinket 3v3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

