
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14652"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14652"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Magnetic Imaging Tile')
    newPart['gitRepo'].append('https://github.com/sparkfun/Magnetic_Imaging_Tile')
    newPart['gitName'].append('Magnetic_Imaging_Tile')
    newPart['eagleBoard'].append('/hardware/Magnetic-Imaging-Tile.brd')
    newPart['eagleSchem'].append('/hardware/Magnetic-Imaging-Tile.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

