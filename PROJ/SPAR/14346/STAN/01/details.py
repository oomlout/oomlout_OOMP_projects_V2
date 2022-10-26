
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14346"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14346"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad ProtoSnap Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_ProtoSnap_Plus')
    newPart['gitName'].append('LilyPad_ProtoSnap_Plus')
    newPart['eagleBoard'].append('/Hardware/LilyPad_ProtoSnap_Plus.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_ProtoSnap_Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

