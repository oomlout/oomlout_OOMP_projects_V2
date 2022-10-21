
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19696"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19696"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Thing Plus DA16200')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Thing_Plus_DA16200')
    newPart['gitName'].append('SparkFun_Thing_Plus_DA16200')
    newPart['eagleBoard'].append('/Hardware/DA16200_Thing_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/DA16200_Thing_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

