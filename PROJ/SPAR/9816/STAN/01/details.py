
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9816"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9816"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OpAmp Breakout LMV358')
    newPart['gitRepo'].append('https://github.com/sparkfun/OpAmp_Breakout-LMV358')
    newPart['gitName'].append('OpAmp_Breakout-LMV358')
    newPart['eagleBoard'].append('/Hardware/SparkFun_OpAmp_Breakout-LMV358.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_OpAmp_Breakout-LMV358.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

