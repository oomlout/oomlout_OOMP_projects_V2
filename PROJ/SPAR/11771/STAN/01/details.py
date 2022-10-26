
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11771"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11771"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TXB0104 breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/TXB0104_breakout')
    newPart['gitName'].append('TXB0104_breakout')
    newPart['eagleBoard'].append('/Hardware/TXB0104_breakout.brd')
    newPart['eagleSchem'].append('/Hardware/TXB0104_breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

