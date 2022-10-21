
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19663"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19663"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun MicroMod GNSS Function Board ZED F9P')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_MicroMod_GNSS_Function_Board_ZED-F9P')
    newPart['gitName'].append('SparkFun_MicroMod_GNSS_Function_Board_ZED-F9P')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroMod_GNSS_Function_Board_ZED-F9P.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroMod_GNSS_Function_Board_ZED-F9P.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

