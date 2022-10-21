
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8661"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8661"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Polar Heart Rate Monitor Interface')
    newPart['gitRepo'].append('https://github.com/sparkfun/Polar_Heart_Rate_Monitor_Interface')
    newPart['gitName'].append('Polar_Heart_Rate_Monitor_Interface')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Polar-HeartRate.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Polar-HeartRate.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

