
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13042"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13042"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison PWM Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_PWM_Block')
    newPart['gitName'].append('Edison_PWM_Block')
    newPart['eagleBoard'].append('/Hardware/PWM_Block.brd')
    newPart['eagleSchem'].append('/Hardware/PWM_Block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

