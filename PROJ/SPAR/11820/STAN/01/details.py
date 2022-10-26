
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11820"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11820"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('WS2812 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/WS2812_Breakout')
    newPart['gitName'].append('WS2812_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFunws2812bBreakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFunws2812bBreakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

