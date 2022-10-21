
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13118"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13118"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Servo Trigger')
    newPart['gitRepo'].append('https://github.com/sparkfun/Servo_Trigger')
    newPart['gitName'].append('Servo_Trigger')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Servo_Trigger.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Servo_Trigger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

