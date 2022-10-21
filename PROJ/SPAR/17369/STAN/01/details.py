
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17369"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17369"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun RTK Surveyor')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_RTK_Surveyor')
    newPart['gitName'].append('SparkFun_RTK_Surveyor')
    newPart['eagleBoard'].append('/Hardware/SparkFun GPS RTK Surveyor.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun GPS RTK Surveyor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

