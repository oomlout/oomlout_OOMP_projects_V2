
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13279"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13279"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Large Digit Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Large_Digit_Driver')
    newPart['gitName'].append('Large_Digit_Driver')
    newPart['eagleBoard'].append('/Hardware/SparkFunLargeDigitDriver.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFunLargeDigitDriver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

