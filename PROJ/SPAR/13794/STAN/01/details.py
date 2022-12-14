
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13794"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13794"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Blynk Board ESP8266')
    newPart['gitRepo'].append('https://github.com/sparkfun/Blynk_Board_ESP8266')
    newPart['gitName'].append('Blynk_Board_ESP8266')
    newPart['eagleBoard'].append('/Hardware/SparkFun-Blynk-Board-ESP8266.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun-Blynk-Board-ESP8266.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

