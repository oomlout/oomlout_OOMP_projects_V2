
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9110"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9110"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Thumb Joystick Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Thumb_Joystick_Breakout')
    newPart['gitName'].append('Thumb_Joystick_Breakout')
    newPart['eagleBoard'].append('/Hardware/Joystick-Breakout-v12.brd')
    newPart['eagleSchem'].append('/Hardware/Joystick-Breakout-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

