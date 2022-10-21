
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9350"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9350"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Slide Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Slide_Switch')
    newPart['gitName'].append('LilyPad_Slide_Switch')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Slide_Switch.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Slide_Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

