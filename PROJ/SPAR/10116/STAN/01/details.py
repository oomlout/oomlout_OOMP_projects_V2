
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10116"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Arduino Fio')
    newPart['gitRepo'].append('https://github.com/sparkfun/Arduino_Fio')
    newPart['gitName'].append('Arduino_Fio')
    newPart['eagleBoard'].append('/Hardware/ArduinoFio.brd')
    newPart['eagleSchem'].append('/Hardware/ArduinoFio.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

