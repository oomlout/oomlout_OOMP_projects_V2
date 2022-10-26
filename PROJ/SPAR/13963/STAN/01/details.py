
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13963"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13963"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LIS3DH Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LIS3DH_Breakout')
    newPart['gitName'].append('LIS3DH_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LIS3DH-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LIS3DH-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

