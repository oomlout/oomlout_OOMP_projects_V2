
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11008"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11008"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Vibe Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Vibe_Board')
    newPart['gitName'].append('LilyPad_Vibe_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LilyPad_Vibe_Board.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LilyPad_Vibe_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

