
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15441"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15441"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun AS3935 Lightning Detector')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_AS3935_Lightning_Detector')
    newPart['gitName'].append('SparkFun_AS3935_Lightning_Detector')
    newPart['eagleBoard'].append('/Hardware/SparkFun_AS3935_Lightning_Detector.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_AS3935_Lightning_Detector.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

