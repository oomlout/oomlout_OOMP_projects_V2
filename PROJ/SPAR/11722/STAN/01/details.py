
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11722"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11722"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Rotary Encoder Breakout Illuminated')
    newPart['gitRepo'].append('https://github.com/sparkfun/Rotary_Encoder_Breakout-Illuminated')
    newPart['gitName'].append('Rotary_Encoder_Breakout-Illuminated')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Rotary_Encoder-Illuminated.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Rotary_Encoder-Illuminated.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

