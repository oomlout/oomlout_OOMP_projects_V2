
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19311"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun LoRaSerial')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_LoRaSerial')
    newPart['gitName'].append('SparkFun_LoRaSerial')
    newPart['eagleBoard'].append('/Hardware/433MHz/SparkFun LoRaSerial 433MHz - 1W.brd')
    newPart['eagleSchem'].append('/Hardware/433MHz/SparkFun LoRaSerial 433MHz - 1W.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

