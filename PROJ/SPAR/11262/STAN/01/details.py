
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11262"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11262"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ProtoSnap LilyPad Development Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/ProtoSnap-LilyPad_Development_Board')
    newPart['gitName'].append('ProtoSnap-LilyPad_Development_Board')
    newPart['eagleBoard'].append('/Hardware/LilyPad-Dev-v34.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-Dev-v34.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

