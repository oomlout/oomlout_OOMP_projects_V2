
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15335"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15335"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic 9DoF IMU Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_9DoF_IMU_Breakout')
    newPart['gitName'].append('SparkFun_Qwiic_9DoF_IMU_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_IMU_Breakout_ICM-20948.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_IMU_Breakout_ICM-20948.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

