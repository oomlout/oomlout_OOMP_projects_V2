
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19013"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19013"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic ToF Imager VL53L5CX Mini')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_ToF_Imager_VL53L5CX-Mini')
    newPart['gitName'].append('SparkFun_Qwiic_ToF_Imager_VL53L5CX-Mini')
    newPart['eagleBoard'].append('/Hardware/SparkFun Qwiic ToF Imager - VL53L5CX - Mini.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun Qwiic ToF Imager - VL53L5CX - Mini.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

