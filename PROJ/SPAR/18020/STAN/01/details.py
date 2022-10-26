
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18020"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18020"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic 6DoF LSM6DSO')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_6DoF_LSM6DSO')
    newPart['gitName'].append('SparkFun_Qwiic_6DoF_LSM6DSO')
    newPart['eagleBoard'].append('/Hardware/SparkFun_6DoF_LSM6DSO.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_6DoF_LSM6DSO.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

