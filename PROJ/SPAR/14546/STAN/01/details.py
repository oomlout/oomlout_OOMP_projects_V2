
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14546"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14546"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad E Sewing Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_E-Sewing_Kit')
    newPart['gitName'].append('LilyPad_E-Sewing_Kit')
    newPart['eagleBoard'].append('/Hardware/LilyPad-E-Sewing-Kit_v15.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-E-Sewing-Kit_v15.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

