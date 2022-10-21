
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19177"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19177"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun IoT RedBoard ESP32')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_IoT_RedBoard-ESP32')
    newPart['gitName'].append('SparkFun_IoT_RedBoard-ESP32')
    newPart['eagleBoard'].append('/hardware/SparkFun_IoT_RedBoard-ESP32.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_IoT_RedBoard-ESP32.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

