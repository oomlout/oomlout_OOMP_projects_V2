
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9101"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9101"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Protoboard Large')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Protoboard_Large')
    newPart['gitName'].append('LilyPad_Protoboard_Large')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Protoboard_Large.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Protoboard_Large.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

