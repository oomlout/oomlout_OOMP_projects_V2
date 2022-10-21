
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10101"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10101"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Window Comparator')
    newPart['gitRepo'].append('https://github.com/sparkfun/Window_Comparator')
    newPart['gitName'].append('Window_Comparator')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Window_Comparator.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Window_Comparator.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

