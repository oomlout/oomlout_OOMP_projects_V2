
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15316"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15316"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pi Servo Hat')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pi_Servo_Hat')
    newPart['gitName'].append('Pi_Servo_Hat')
    newPart['eagleBoard'].append('/Hardware/Pi_Servo_pHAT.brd')
    newPart['eagleSchem'].append('/Hardware/Pi_Servo_pHAT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

