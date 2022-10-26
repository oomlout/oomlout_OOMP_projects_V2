
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10941"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10941"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Arduino SimpleSnap')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Arduino_SimpleSnap')
    newPart['gitName'].append('LilyPad_Arduino_SimpleSnap')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Arduino_SimpleSnap.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Arduino_SimpleSnap.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

