
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16988"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16988"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QwiicBus EndPoint')
    newPart['gitRepo'].append('https://github.com/sparkfun/QwiicBus_EndPoint')
    newPart['gitName'].append('QwiicBus_EndPoint')
    newPart['eagleBoard'].append('/Hardware/SparkFun_QwiicBus_Endpoint.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_QwiicBus_Endpoint.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

