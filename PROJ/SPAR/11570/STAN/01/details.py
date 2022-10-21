
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11570"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11570"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TRRS 3.5mm Jack Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/TRRS_3.5mm_Jack_Breakout')
    newPart['gitName'].append('TRRS_3.5mm_Jack_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TRRS_3.5mm_Jack_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TRRS_3.5mm_Jack_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

