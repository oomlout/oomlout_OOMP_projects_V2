
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15795"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15795"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pro Micro')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pro_Micro')
    newPart['gitName'].append('Pro_Micro')
    newPart['eagleBoard'].append('/Hardware/v13/SparkFun_Pro_Micro.brd')
    newPart['eagleSchem'].append('/Hardware/v13/SparkFun_Pro_Micro.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

