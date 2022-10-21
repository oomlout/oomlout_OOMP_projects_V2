
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8937"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8937"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad XBee')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_XBee')
    newPart['gitName'].append('LilyPad_XBee')
    newPart['eagleBoard'].append('/Hardware/LilyPad_XBee.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_XBee.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

