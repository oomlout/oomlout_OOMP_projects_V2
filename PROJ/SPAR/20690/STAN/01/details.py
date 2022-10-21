
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20690"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20690"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic Speaker Amp')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_Speaker_Amp')
    newPart['gitName'].append('SparkFun_Qwiic_Speaker_Amp')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_Speaker_Amp.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_Speaker_Amp.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

