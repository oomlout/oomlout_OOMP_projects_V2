
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10615"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10615"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('PWM Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/PWM_Shield')
    newPart['gitName'].append('PWM_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_PWM_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_PWM_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

