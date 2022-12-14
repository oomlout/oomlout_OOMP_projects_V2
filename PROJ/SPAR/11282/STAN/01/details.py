
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11282"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11282"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BMP085 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/BMP085_Breakout')
    newPart['gitName'].append('BMP085_Breakout')
    newPart['eagleBoard'].append('/Hardware/BMP085 Breakout-v14.brd')
    newPart['eagleSchem'].append('/Hardware/BMP085 Breakout-v14.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

