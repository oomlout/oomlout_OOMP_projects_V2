
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0747"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0747"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LMD1820x Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LMD1820x_Breakout')
    newPart['gitName'].append('LMD1820x_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LMD1820x-Breakout-V12.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LMD1820x-Breakout-V12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

