
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9235"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SPI Shortcut')
    newPart['gitRepo'].append('https://github.com/sparkfun/SPI_Shortcut')
    newPart['gitName'].append('SPI_Shortcut')
    newPart['eagleBoard'].append('/Hardware/SPIShortcut.brd')
    newPart['eagleSchem'].append('/Hardware/SPIShortcut.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

