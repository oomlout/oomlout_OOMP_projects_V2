
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13155"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13155"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Stepoko')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Stepoko')
    newPart['gitName'].append('SparkFun_Stepoko')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Stepoko.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Stepoko.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

