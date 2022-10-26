
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13762"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MPU 9250 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MPU-9250_Breakout')
    newPart['gitName'].append('MPU-9250_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MPU-9250_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MPU-9250_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

