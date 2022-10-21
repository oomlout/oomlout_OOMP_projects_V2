
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13288"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13288"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Teensy Arduino Shield Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Teensy_Arduino_Shield_Adapter')
    newPart['gitName'].append('Teensy_Arduino_Shield_Adapter')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Teensy_Adapter.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Teensy_Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

