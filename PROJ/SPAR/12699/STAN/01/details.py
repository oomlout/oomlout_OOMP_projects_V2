
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12699"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12699"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Solderable Breadboard Large')
    newPart['gitRepo'].append('https://github.com/sparkfun/Solderable_Breadboard_Large')
    newPart['gitName'].append('Solderable_Breadboard_Large')
    newPart['eagleBoard'].append('/hardware/Solderable_Breadboard_Large.brd')
    newPart['eagleSchem'].append('/hardware/Solderable_Breadboard_Large.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

