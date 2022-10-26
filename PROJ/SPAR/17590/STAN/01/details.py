
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17590"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17590"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Haptic Driver DA7280')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Haptic_Driver_DA7280')
    newPart['gitName'].append('Qwiic_Haptic_Driver_DA7280')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Haptic_Driver_DA7280.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Haptic_Driver_DA7280.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

