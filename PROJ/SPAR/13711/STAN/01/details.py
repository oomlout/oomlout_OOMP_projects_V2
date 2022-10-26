
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13711"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13711"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ESP8266 Thing Dev 4H')
    newPart['gitRepo'].append('https://github.com/sparkfun/ESP8266_Thing_Dev_4H')
    newPart['gitName'].append('ESP8266_Thing_Dev_4H')
    newPart['eagleBoard'].append('/Hardware/ESP8266-Thing-Dev-4H.brd')
    newPart['eagleSchem'].append('/Hardware/ESP8266-Thing-Dev-4H.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

