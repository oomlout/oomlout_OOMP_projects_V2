
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10889"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10889"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ProtoSnap Pro Mini')
    newPart['gitRepo'].append('https://github.com/sparkfun/ProtoSnap-Pro_Mini')
    newPart['gitName'].append('ProtoSnap-Pro_Mini')
    newPart['eagleBoard'].append('/Hardware/ProtoSnap-v14a.brd')
    newPart['eagleSchem'].append('/Hardware/ProtoSnap-v14a.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

