
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10680"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10680"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Shift Register Breakout 74HC595')
    newPart['gitRepo'].append('https://github.com/sparkfun/Shift_Register_Breakout-74HC595')
    newPart['gitName'].append('Shift_Register_Breakout-74HC595')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Shift_Register_Breakout-74HC595.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Shift_Register_Breakout-74HC595.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

