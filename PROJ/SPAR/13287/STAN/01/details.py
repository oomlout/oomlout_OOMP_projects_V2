
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13287"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13287"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP8266 WiFi Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP8266_WiFi_Shield')
    newPart['gitName'].append('ESP8266_WiFi_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun-ESP8266-WiFi-Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun-ESP8266-WiFi-Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

