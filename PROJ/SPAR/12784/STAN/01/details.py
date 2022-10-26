
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12784"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12784"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ToF Range Finder Breakout VL6180')
    newPart['gitRepo'].append('https://github.com/sparkfun/ToF_Range_Finder_Breakout-VL6180')
    newPart['gitName'].append('ToF_Range_Finder_Breakout-VL6180')
    newPart['eagleBoard'].append('/Hardware/SparkFun_VL6180_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_VL6180_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

