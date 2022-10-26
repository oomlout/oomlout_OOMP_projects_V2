
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13926"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13926"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MMA8452 Accelerometer')
    newPart['gitRepo'].append('https://github.com/sparkfun/MMA8452_Accelerometer')
    newPart['gitName'].append('MMA8452_Accelerometer')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MMA8452Q-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MMA8452Q-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

