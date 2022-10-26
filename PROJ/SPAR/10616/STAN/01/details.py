
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10616"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10616"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LED Driver Breakout TLC5940')
    newPart['gitRepo'].append('https://github.com/sparkfun/LED_Driver_Breakout-TLC5940')
    newPart['gitName'].append('LED_Driver_Breakout-TLC5940')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TLC5940_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TLC5940_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

