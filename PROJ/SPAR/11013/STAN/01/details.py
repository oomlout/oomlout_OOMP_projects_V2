
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11013"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11013"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad MP3 Player')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_MP3_Player')
    newPart['gitName'].append('LilyPad_MP3_Player')
    newPart['eagleBoard'].append('/hardware/LilyPad-MP3-v15a.brd')
    newPart['eagleSchem'].append('/hardware/LilyPad-MP3-v15a.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

