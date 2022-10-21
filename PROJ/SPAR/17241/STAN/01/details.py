
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17241"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17241"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic ADXL313')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_ADXL313')
    newPart['gitName'].append('SparkFun_Qwiic_ADXL313')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_ADXL313.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_ADXL313.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

