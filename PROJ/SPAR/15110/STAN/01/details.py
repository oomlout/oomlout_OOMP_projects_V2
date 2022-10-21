
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15110"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15110"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun ESP32 Thing Plus DMX to LED Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_ESP32_Thing_Plus_DMX_to_LED_Shield')
    newPart['gitName'].append('SparkFun_ESP32_Thing_Plus_DMX_to_LED_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun ESP32 Thing Plus DMX to LED Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun ESP32 Thing Plus DMX to LED Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

