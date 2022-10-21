
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12707"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12707"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Sparkpunk Sequencer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Sparkpunk_Sequencer')
    newPart['gitName'].append('Sparkpunk_Sequencer')
    newPart['eagleBoard'].append('/hardware/sparkpunk_sequencer.brd')
    newPart['eagleSchem'].append('/hardware/sparkpunk_sequencer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

