
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13968"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13968"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OpenPIR')
    newPart['gitRepo'].append('https://github.com/sparkfun/OpenPIR')
    newPart['gitName'].append('OpenPIR')
    newPart['eagleBoard'].append('/Hardware/SparkFun-OpenPIR-NCS36000.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun-OpenPIR-NCS36000.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

