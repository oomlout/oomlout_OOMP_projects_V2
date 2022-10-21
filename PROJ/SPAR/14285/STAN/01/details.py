
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14285"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14285"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Wireless Motor Driver Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Wireless_Motor_Driver_Shield')
    newPart['gitName'].append('Wireless_Motor_Driver_Shield')
    newPart['eagleBoard'].append('/hardware/Wireless_Motor_Driver_Shield.brd')
    newPart['eagleSchem'].append('/hardware/Wireless_Motor_Driver_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

