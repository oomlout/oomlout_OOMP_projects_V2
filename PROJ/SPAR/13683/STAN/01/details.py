
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13683"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13683"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SHT15 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SHT15_Breakout')
    newPart['gitName'].append('SHT15_Breakout')
    newPart['eagleBoard'].append('/Hardware/SHT1x-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SHT1x-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

