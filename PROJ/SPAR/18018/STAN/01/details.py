
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18018"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18018"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun ESP32 Thing Plus C')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_ESP32_Thing_Plus_C')
    newPart['gitName'].append('SparkFun_ESP32_Thing_Plus_C')
    newPart['eagleBoard'].append('/Hardware/SparkFun ESP32 Thing Plus C.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun ESP32 Thing Plus C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

