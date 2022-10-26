
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14063"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14063"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad LilyMini ProtoSnap')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_LilyMini_ProtoSnap')
    newPart['gitName'].append('LilyPad_LilyMini_ProtoSnap')
    newPart['eagleBoard'].append('/Hardware/LilyMini_Protosnap.brd')
    newPart['eagleSchem'].append('/Hardware/LilyMini_Protosnap.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

