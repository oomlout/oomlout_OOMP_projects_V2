
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11824"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11824"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BMP180 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/BMP180_Breakout')
    newPart['gitName'].append('BMP180_Breakout')
    newPart['eagleBoard'].append('/hardware/SparkFun_BMP180_Breakout.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_BMP180_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

