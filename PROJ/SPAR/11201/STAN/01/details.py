
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11201"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11201"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ProtoSnap LilyPad Dev Simple')
    newPart['gitRepo'].append('https://github.com/sparkfun/ProtoSnap-LilyPad_Dev_Simple')
    newPart['gitName'].append('ProtoSnap-LilyPad_Dev_Simple')
    newPart['eagleBoard'].append('/Hardware/LilyPad-Dev-Simple-v12.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-Dev-Simple-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

