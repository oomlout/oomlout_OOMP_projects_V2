
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17745"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17745"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Thing Plus RP2040')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Thing_Plus-RP2040')
    newPart['gitName'].append('SparkFun_Thing_Plus-RP2040')
    newPart['eagleBoard'].append('/Hardware/RP2040_Thing_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/RP2040_Thing_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

