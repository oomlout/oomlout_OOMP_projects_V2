
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13162"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13162"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ZX Gesture Sensor SMD')
    newPart['gitRepo'].append('https://github.com/sparkfun/ZX_Gesture_Sensor_SMD')
    newPart['gitName'].append('ZX_Gesture_Sensor_SMD')
    newPart['eagleBoard'].append('/Hardware/ZX_Gesture_Sensor_SMD.brd')
    newPart['eagleSchem'].append('/Hardware/ZX_Gesture_Sensor_SMD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

