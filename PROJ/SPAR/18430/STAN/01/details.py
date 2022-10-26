
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18430"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18430"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun WiFi Function Board ESP32')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_WiFi_Function_Board_ESP32')
    newPart['gitName'].append('SparkFun_WiFi_Function_Board_ESP32')
    newPart['eagleBoard'].append('/Hardware/ESP32-Function.brd')
    newPart['eagleSchem'].append('/Hardware/ESP32-Function.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

