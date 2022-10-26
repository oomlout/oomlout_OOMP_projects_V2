
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13311"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Teensy 3 1 XBee Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Teensy_3_1_XBee_Adapter')
    newPart['gitName'].append('Teensy_3_1_XBee_Adapter')
    newPart['eagleBoard'].append('/Hardware/Teensy_3_1 XBee _Adapter.brd')
    newPart['eagleSchem'].append('/Hardware/Teensy_3_1 XBee _Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

