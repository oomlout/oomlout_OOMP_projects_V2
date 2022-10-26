
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12849"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12849"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RN 52')
    newPart['gitRepo'].append('https://github.com/sparkfun/RN-52')
    newPart['gitName'].append('RN-52')
    newPart['eagleBoard'].append('/Hardware/SparkFun_RN-52_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_RN-52_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

