
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9102"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9102"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Protoboard Small')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Protoboard_Small')
    newPart['gitName'].append('LilyPad_Protoboard_Small')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Protoboard_Small.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Protoboard_Small.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

