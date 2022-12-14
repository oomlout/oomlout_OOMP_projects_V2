
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14721"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14721"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RGB Panel Arduino Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/RGB_Panel_Arduino_Shield')
    newPart['gitName'].append('RGB_Panel_Arduino_Shield')
    newPart['eagleBoard'].append('/Hardware/RGB Panel Shield for Arduino.brd')
    newPart['eagleSchem'].append('/Hardware/RGB Panel Shield for Arduino.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

