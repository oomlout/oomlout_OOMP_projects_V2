
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14203"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14203"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for ESP32')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_ESP32')
    newPart['gitName'].append('Qwiic_Shield_for_ESP32')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_Qwiic_Shield_for_ESP32.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_Qwiic_Shield_for_ESP32.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

