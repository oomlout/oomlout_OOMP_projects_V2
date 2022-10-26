
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13884"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13884"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LP55231 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LP55231_Breakout')
    newPart['gitName'].append('LP55231_Breakout')
    newPart['eagleBoard'].append('/Hardware/LP55231_breakout.brd')
    newPart['eagleSchem'].append('/Hardware/LP55231_breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

