
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10401"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10401"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Lipo Charger Basic miniUSB')
    newPart['gitRepo'].append('https://github.com/sparkfun/Lipo_Charger_Basic-miniUSB')
    newPart['gitName'].append('Lipo_Charger_Basic-miniUSB')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LiPo-Charger-Basic-MiniUSB.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LiPo-Charger-Basic-MiniUSB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

