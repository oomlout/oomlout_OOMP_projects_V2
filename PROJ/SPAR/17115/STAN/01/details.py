
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17115"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17115"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SerialFlash Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SerialFlash-Breakout')
    newPart['gitName'].append('SerialFlash-Breakout')
    newPart['eagleBoard'].append('/Hardware/QSPI-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/QSPI-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

