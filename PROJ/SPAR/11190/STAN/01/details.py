
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11190"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11190"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Arduino USB')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Arduino_USB')
    newPart['gitName'].append('LilyPad_Arduino_USB')
    newPart['eagleBoard'].append('/Hardware/Lilypad_Arduino_USB.brd')
    newPart['eagleSchem'].append('/Hardware/Lilypad_Arduino_USB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

