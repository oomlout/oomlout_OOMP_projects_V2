
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16781"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16781"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod ESP32 Processor')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_ESP32_Processor')
    newPart['gitName'].append('MicroMod_ESP32_Processor')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroMod_ESP32.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroMod_ESP32.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

