
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11858"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11858"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Copernicus II DIP Module')
    newPart['gitRepo'].append('https://github.com/sparkfun/Copernicus_II_DIP_Module')
    newPart['gitName'].append('Copernicus_II_DIP_Module')
    newPart['eagleBoard'].append('/Hardware/Copernicus-DIP-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Copernicus-DIP-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

