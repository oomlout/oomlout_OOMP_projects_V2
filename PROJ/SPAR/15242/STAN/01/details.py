
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15242"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15242"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Scale')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Scale')
    newPart['gitName'].append('Qwiic_Scale')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Scale.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Scale.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

