
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11420"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11420"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MiniGen')
    newPart['gitRepo'].append('https://github.com/sparkfun/MiniGen')
    newPart['gitName'].append('MiniGen')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MiniGen.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MiniGen.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

