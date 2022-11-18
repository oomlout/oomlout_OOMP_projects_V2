
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP32 LoRa 1CH Gateway')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP32_LoRa_1CH_Gateway')
    newPart['gitName'].append('ESP32_LoRa_1CH_Gateway')
    newPart['eagleBoard'].append('/Hardware/ESP32_LoRa_1_Channel_Gateway.brd')
    newPart['eagleSchem'].append('/Hardware/ESP32_LoRa_1_Channel_Gateway.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

