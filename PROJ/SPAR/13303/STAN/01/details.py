
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13303"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13303"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LSM303C 6 DOF IMU Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LSM303C_6_DOF_IMU_Breakout')
    newPart['gitName'].append('LSM303C_6_DOF_IMU_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LSM303C_6_DOF_IMU_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LSM303C_6_DOF_IMU_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

