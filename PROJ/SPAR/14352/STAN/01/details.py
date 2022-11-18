
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14352"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14352"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for Arduino')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_Arduino')
    newPart['gitName'].append('Qwiic_Shield_for_Arduino')
    newPart['eagleBoard'].append('/Hardware/Qwiic Shield for Arduino.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Shield for Arduino.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

