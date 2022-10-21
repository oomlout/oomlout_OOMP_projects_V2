
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11590"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11590"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyTwinkle ProtoSnap')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyTwinkle_ProtoSnap')
    newPart['gitName'].append('LilyTwinkle_ProtoSnap')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ProtoSnap-LilyTwinkle.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ProtoSnap-LilyTwinkle.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

