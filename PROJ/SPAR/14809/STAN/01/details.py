
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14809"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14809"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('I2S Audio Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/I2S_Audio_Breakout')
    newPart['gitName'].append('I2S_Audio_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_I2S_Audio_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_I2S_Audio_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

