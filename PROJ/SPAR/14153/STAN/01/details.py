
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14153"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14153"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP32 Environment Sensor Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP32_Environment_Sensor_Shield')
    newPart['gitName'].append('ESP32_Environment_Sensor_Shield')
    newPart['eagleBoard'].append('/Hardware/sparkfun_esp32_environment_sensor_shield.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun_esp32_environment_sensor_shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

