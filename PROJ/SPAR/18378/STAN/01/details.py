
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18378"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18378"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun GNSS Function Board NEO M9N')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_GNSS_Function_Board_NEO-M9N')
    newPart['gitName'].append('SparkFun_GNSS_Function_Board_NEO-M9N')
    newPart['eagleBoard'].append('/Hardware/SparkFun_GNSS_NEO-M9N.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_GNSS_NEO-M9N.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

