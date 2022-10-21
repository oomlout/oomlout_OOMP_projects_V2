
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13795"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13795"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LED Array 8x7')
    newPart['gitRepo'].append('https://github.com/sparkfun/LED_Array_8x7')
    newPart['gitName'].append('LED_Array_8x7')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LED_Array_8x7.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LED_Array_8x7.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

