
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9773"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9773"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Fuse Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun-Fuse-Breakout-Board')
    newPart['gitName'].append('SparkFun-Fuse-Breakout-Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun Fuse Breakout Board.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun Fuse Breakout Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

