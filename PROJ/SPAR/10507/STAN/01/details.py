
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10507"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10507"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Quadstepper Motor Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Quadstepper_Motor_Driver')
    newPart['gitName'].append('Quadstepper_Motor_Driver')
    newPart['eagleBoard'].append('/Hardware/SparkFun_quadstep-v11assembly.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_quadstep-v11assembly.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

