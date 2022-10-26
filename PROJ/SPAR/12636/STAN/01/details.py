
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12636"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LSM9DS0 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LSM9DS0_Breakout')
    newPart['gitName'].append('LSM9DS0_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_lsm9ds0-breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_lsm9ds0-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

