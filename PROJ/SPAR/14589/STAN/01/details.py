
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14589"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14589"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Differential I2C Breakout PCA9615 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Differential_I2C_Breakout_PCA9615_Qwiic')
    newPart['gitName'].append('SparkFun_Differential_I2C_Breakout_PCA9615_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Differential_I2C_Breakout_PCA9615_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Differential_I2C_Breakout_PCA9615_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

