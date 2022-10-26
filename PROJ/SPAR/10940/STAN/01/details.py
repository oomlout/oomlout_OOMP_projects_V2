
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10940"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10940"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad SimpleSnap Protoboard')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_SimpleSnap_Protoboard')
    newPart['gitName'].append('LilyPad_SimpleSnap_Protoboard')
    newPart['eagleBoard'].append('/Hardware/LilyPad_SimpleSnap_ProtoBoard.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_SimpleSnap_ProtoBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

