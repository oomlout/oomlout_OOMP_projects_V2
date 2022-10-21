
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13343"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13343"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Reed Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Reed_Switch')
    newPart['gitName'].append('LilyPad_Reed_Switch')
    newPart['eagleBoard'].append('/Hardware/LilyPad-reed.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-reed.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

