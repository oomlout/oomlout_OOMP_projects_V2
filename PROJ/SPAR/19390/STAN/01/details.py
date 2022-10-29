
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19390"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19390"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun u blox NEO D9S')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_u-blox_NEO-D9S')
    newPart['gitName'].append('SparkFun_u-blox_NEO-D9S')
    newPart['eagleBoard'].append('/Hardware/SparkFun NEO-D9S.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun NEO-D9S.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

