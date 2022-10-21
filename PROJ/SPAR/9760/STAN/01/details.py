
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9760"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9760"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Joystick Shield Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Joystick_Shield_Kit')
    newPart['gitName'].append('Joystick_Shield_Kit')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Joystick_Shield_Kit.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Joystick_Shield_Kit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

