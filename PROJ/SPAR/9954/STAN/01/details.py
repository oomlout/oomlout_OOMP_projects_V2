
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9954"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9954"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('WiFly Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/WiFly-Shield')
    newPart['gitName'].append('WiFly-Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_WiFly_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_WiFly_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

