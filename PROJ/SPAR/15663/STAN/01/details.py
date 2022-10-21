
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15663"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15663"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP32 Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP32_Thing_Plus')
    newPart['gitName'].append('ESP32_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/ESP32_Thing_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/ESP32_Thing_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

