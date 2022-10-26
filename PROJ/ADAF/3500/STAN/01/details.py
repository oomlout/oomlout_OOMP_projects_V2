
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3500"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3500"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Trinket M0 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Trinket-M0-PCB')
    newPart['gitName'].append('Adafruit-Trinket-M0-PCB')
    newPart['eagleBoard'].append('/Trinket M0 rev D.brd')
    newPart['eagleSchem'].append('/Trinket M0 rev D.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

