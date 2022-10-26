
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "7841"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR7841"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FT245RL Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/FT245RL_Breakout')
    newPart['gitName'].append('FT245RL_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_FT245-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_FT245-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

