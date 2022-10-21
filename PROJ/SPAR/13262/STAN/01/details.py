
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13262"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13262"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CAN Bus Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/CAN-Bus_Shield')
    newPart['gitName'].append('CAN-Bus_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_CAN-Bus_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_CAN-Bus_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

