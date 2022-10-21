
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13261"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13261"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OpenScale')
    newPart['gitRepo'].append('https://github.com/sparkfun/OpenScale')
    newPart['gitName'].append('OpenScale')
    newPart['eagleBoard'].append('/hardware/SparkFun_openScale.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_openScale.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

