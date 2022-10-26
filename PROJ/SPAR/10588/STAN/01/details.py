
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10588"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10588"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Audio Jack Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Audio_Jack_Breakout')
    newPart['gitName'].append('Audio_Jack_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Audio_Jack_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Audio_Jack_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

