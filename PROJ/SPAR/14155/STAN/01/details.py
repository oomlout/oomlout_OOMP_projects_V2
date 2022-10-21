
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14155"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14155"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP32 Power Control Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP32_Power_Control_Shield')
    newPart['gitName'].append('ESP32_Power_Control_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ESP32_Power_Control_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ESP32_Power_Control_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

