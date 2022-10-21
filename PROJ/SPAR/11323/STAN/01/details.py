
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11323"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11323"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('EL Sequencer')
    newPart['gitRepo'].append('https://github.com/sparkfun/EL_Sequencer')
    newPart['gitName'].append('EL_Sequencer')
    newPart['eagleBoard'].append('/Hardware/EL_Sequencer.brd')
    newPart['eagleSchem'].append('/Hardware/EL_Sequencer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

