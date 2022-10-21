
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10217"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10217"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Lipo Charger Basic microUSB')
    newPart['gitRepo'].append('https://github.com/sparkfun/Lipo_Charger_Basic-microUSB')
    newPart['gitName'].append('Lipo_Charger_Basic-microUSB')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Lipo_Charger_Basic-microUSB.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Lipo_Charger_Basic-microUSB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

