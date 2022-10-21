
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10743"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10743"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mega Pro Mini')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mega_Pro_Mini')
    newPart['gitName'].append('Mega_Pro_Mini')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Mega_Pro_Mini-3.3V.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Mega_Pro_Mini-3.3V.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

