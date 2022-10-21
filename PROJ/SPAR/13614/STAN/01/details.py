
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13614"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13614"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qduino Mini SFE')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qduino_Mini_SFE')
    newPart['gitName'].append('Qduino_Mini_SFE')
    newPart['eagleBoard'].append('/Hardware/Qduino_Mini.brd')
    newPart['eagleSchem'].append('/Hardware/Qduino_Mini.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

