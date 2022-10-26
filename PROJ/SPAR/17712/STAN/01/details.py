
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17712"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17712"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('STM32 Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/STM32_Thing_Plus')
    newPart['gitName'].append('STM32_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/SparkFun_STM32 Thing Plus.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_STM32 Thing Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

