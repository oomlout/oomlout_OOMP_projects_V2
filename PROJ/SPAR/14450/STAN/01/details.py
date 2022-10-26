
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14450"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14450"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Motor Driver Dual TB6612FNG')
    newPart['gitRepo'].append('https://github.com/sparkfun/Motor_Driver-Dual_TB6612FNG')
    newPart['gitName'].append('Motor_Driver-Dual_TB6612FNG')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Motor_Driver-TB6612FNG_v11.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Motor_Driver-TB6612FNG_v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

