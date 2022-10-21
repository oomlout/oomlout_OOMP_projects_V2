
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18712"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18712"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Artemis Global Tracker')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Artemis_Global_Tracker')
    newPart['gitName'].append('SparkFun_Artemis_Global_Tracker')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Artemis_Global_Tracker.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Artemis_Global_Tracker.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

