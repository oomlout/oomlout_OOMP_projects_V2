
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19921"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19921"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic Magnetometer MMC5983MA')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_Magnetometer-MMC5983MA')
    newPart['gitName'].append('SparkFun_Qwiic_Magnetometer-MMC5983MA')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Magnetometer_MMC5983MA_Qwiic_Micro.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Magnetometer_MMC5983MA_Qwiic_Micro.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

