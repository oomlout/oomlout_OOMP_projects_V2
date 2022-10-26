
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15193"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun u blox ZOE M8Q')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_u-blox_ZOE-M8Q')
    newPart['gitName'].append('SparkFun_u-blox_ZOE-M8Q')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ZOE-M8Q GPS.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ZOE-M8Q GPS.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

