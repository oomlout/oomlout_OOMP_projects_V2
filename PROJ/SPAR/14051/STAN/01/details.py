
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14051"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14051"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Wireless Joystick')
    newPart['gitRepo'].append('https://github.com/sparkfun/Wireless_Joystick')
    newPart['gitName'].append('Wireless_Joystick')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Wireless_JoyStick.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Wireless_JoyStick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

