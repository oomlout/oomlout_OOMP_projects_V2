
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12581"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12581"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RooTooth')
    newPart['gitRepo'].append('https://github.com/sparkfun/RooTooth')
    newPart['gitName'].append('RooTooth')
    newPart['eagleBoard'].append('/Hardware/RN41_Rootooth.brd')
    newPart['eagleSchem'].append('/Hardware/RN41_Rootooth.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

