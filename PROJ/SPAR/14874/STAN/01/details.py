
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14874"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14874"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TSH82 Configurable Op Amp Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/TSH82_Configurable_Op_Amp_Board')
    newPart['gitName'].append('TSH82_Configurable_Op_Amp_Board')
    newPart['eagleBoard'].append('/Hardware/TSH82_Configurable_Op_Amp_Board.brd')
    newPart['eagleSchem'].append('/Hardware/TSH82_Configurable_Op_Amp_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

