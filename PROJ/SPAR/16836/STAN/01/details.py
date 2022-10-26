
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16836"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16836"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun ProDriver TC78H670FTG')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_ProDriver_TC78H670FTG')
    newPart['gitName'].append('SparkFun_ProDriver_TC78H670FTG')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ProDriver_TC78H670FTG.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ProDriver_TC78H670FTG.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

