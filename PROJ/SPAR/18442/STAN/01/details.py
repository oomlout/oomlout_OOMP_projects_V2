
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18442"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18442"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun RTK Express')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_RTK_Express')
    newPart['gitName'].append('SparkFun_RTK_Express')
    newPart['eagleBoard'].append('/Hardware/SparkFun RTK Express.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun RTK Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

