
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16789"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16789"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for Arduino Nano')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_Arduino_Nano')
    newPart['gitName'].append('Qwiic_Shield_for_Arduino_Nano')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Shield_for_Arduino_Nano.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Shield_for_Arduino_Nano.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

