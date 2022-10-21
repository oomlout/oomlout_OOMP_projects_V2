
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15734"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15734"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Clock Generator 5P49V60')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Clock_Generator_5P49V60')
    newPart['gitName'].append('SparkFun_Clock_Generator_5P49V60')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Clock_Generator_5PV49V60.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Clock_Generator_5PV49V60.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

