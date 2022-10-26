
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9836"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9836"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL345 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ADXL345_Breakout')
    newPart['gitName'].append('ADXL345_Breakout')
    newPart['eagleBoard'].append('/Hardware/ADXL345_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/ADXL345_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

