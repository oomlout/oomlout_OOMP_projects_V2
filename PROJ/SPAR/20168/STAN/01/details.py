
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20168"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20168"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Thing Plus ESP32 WROOM C')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Thing_Plus_ESP32_WROOM_C')
    newPart['gitName'].append('SparkFun_Thing_Plus_ESP32_WROOM_C')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Thing_Plus_ESP32_WROOM_C.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Thing_Plus_ESP32_WROOM_C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

