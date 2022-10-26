
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15173"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15173"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Transparent Graphical OLED')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Transparent_Graphical_OLED')
    newPart['gitName'].append('Qwiic_Transparent_Graphical_OLED')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Transparent_Graphical_OLED_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Transparent_Graphical_OLED_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

