
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13741"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13741"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedStick')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedStick')
    newPart['gitName'].append('RedStick')
    newPart['eagleBoard'].append('/Hardware/SparkFun_RedStick.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_RedStick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

