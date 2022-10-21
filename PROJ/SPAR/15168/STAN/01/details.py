
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15168"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15168"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Joystick')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Joystick')
    newPart['gitName'].append('Qwiic_Joystick')
    newPart['eagleBoard'].append('/Hardware/Qwiic Joystick_Eagle/Qwiic Joystick.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Joystick_Eagle/Qwiic Joystick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

