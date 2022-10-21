
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9540"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9540"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Full Bridge Motor Driver Breakout L298N')
    newPart['gitRepo'].append('https://github.com/sparkfun/Full_Bridge_Motor_Driver_Breakout-L298N')
    newPart['gitName'].append('Full_Bridge_Motor_Driver_Breakout-L298N')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Full_Bridge_Motor_Driver_Breakout-L298N.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Full_Bridge_Motor_Driver_Breakout-L298N.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

