
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17381"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17381"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP32 Thing Plus U.FL')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP32_Thing_Plus_U.FL')
    newPart['gitName'].append('ESP32_Thing_Plus_U.FL')
    newPart['eagleBoard'].append('/Hardware/ESP32_Thing_Plus_UFL.brd')
    newPart['eagleSchem'].append('/Hardware/ESP32_Thing_Plus_UFL.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

