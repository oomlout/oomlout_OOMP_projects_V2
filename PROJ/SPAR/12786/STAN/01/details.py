
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12786"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12786"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL337 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ADXL337_Breakout')
    newPart['gitName'].append('ADXL337_Breakout')
    newPart['eagleBoard'].append('/hardware/ADXL337 Breakout.brd')
    newPart['eagleSchem'].append('/hardware/ADXL337 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

