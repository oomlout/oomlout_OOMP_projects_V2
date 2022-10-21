
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16328"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16328"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Auto pHAT')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Auto_pHAT')
    newPart['gitName'].append('SparkFun_Auto_pHAT')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Auto_pHAT.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Auto_pHAT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

