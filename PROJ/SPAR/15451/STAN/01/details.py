
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15451"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15451"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Motor Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Motor_Driver')
    newPart['gitName'].append('Qwiic_Motor_Driver')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_Motor_Driver.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_Motor_Driver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

