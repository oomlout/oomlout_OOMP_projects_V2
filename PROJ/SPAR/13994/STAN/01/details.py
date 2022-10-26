
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13994"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13994"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SSOP DIP Adapter 16 Pin')
    newPart['gitRepo'].append('https://github.com/sparkfun/SSOP-DIP_Adapter_16-Pin')
    newPart['gitName'].append('SSOP-DIP_Adapter_16-Pin')
    newPart['eagleBoard'].append('/Hardware/SparkFun_SSOP16_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_SSOP16_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

