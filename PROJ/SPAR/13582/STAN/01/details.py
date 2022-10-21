
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13582"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13582"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Line Follower Array')
    newPart['gitRepo'].append('https://github.com/sparkfun/Line_Follower_Array')
    newPart['gitName'].append('Line_Follower_Array')
    newPart['eagleBoard'].append('/Hardware/SparkFun Line Follower Array.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun Line Follower Array.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

