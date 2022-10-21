
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12070"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12070"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Solder able Breadboard')
    newPart['gitRepo'].append('https://github.com/sparkfun/Solder-able_Breadboard')
    newPart['gitName'].append('Solder-able_Breadboard')
    newPart['eagleBoard'].append('/hardware/SIK-DIP-board.brd')
    newPart['eagleSchem'].append('/hardware/SIK-DIP-board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

