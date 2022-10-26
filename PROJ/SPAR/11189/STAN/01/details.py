
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11189"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11189"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MAX3232 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MAX3232_Breakout')
    newPart['gitName'].append('MAX3232_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MAX3232_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MAX3232_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

