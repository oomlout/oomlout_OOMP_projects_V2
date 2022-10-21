
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14430"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14430"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP32 Motion Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP32_Motion_Shield')
    newPart['gitName'].append('ESP32_Motion_Shield')
    newPart['eagleBoard'].append('/Hardware/ESP32_GPS_Motion_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/ESP32_GPS_Motion_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

