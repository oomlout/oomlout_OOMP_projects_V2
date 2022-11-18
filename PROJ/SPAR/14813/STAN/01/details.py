
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14813"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14813"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic SGP30 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic-SGP30-Breakout')
    newPart['gitName'].append('Qwiic-SGP30-Breakout')
    newPart['eagleBoard'].append('/Hardware/SGP30 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SGP30 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

