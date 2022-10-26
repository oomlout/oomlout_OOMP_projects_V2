
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18037"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18037"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun u blox MAX M10S')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_u-blox_MAX-M10S')
    newPart['gitName'].append('SparkFun_u-blox_MAX-M10S')
    newPart['eagleBoard'].append('/Hardware/SparkFun u-blox GNSS MAX-M10S.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun u-blox GNSS MAX-M10S.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

