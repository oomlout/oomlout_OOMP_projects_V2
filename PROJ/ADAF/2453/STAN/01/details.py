
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2453"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2453"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DPI Kippah PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DPI-Kippah-PCB')
    newPart['gitName'].append('Adafruit-DPI-Kippah-PCB')
    newPart['eagleBoard'].append('/Adafruit DPI Kippah.brd')
    newPart['eagleSchem'].append('/Adafruit DPI Kippah.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

