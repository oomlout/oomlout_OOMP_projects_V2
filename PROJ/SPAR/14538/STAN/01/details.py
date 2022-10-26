
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14538"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14538"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Haptic Motor Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Haptic_Motor_Driver')
    newPart['gitName'].append('Haptic_Motor_Driver')
    newPart['eagleBoard'].append('/Hardware/Haptic_Motor_Driver_DRV2605L_v20.brd')
    newPart['eagleSchem'].append('/Hardware/Haptic_Motor_Driver_DRV2605L_v20.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

