
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15031"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15031"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/ESP8266 WiFi IR Blaster')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/ESP8266_WiFi_IR_Blaster')
    newPart['gitName'].append('https://github.com/sparkfunX/ESP8266_WiFi_IR_Blaster')
    newPart['eagleBoard'].append('sourceFiles/git/ESP8266_WiFi_IR_Blaster/Hardware/esp8266_ir_blaster.brd')
    newPart['eagleSchem'].append('sourceFiles/git/ESP8266_WiFi_IR_Blaster/Hardware/esp8266_ir_blaster.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

