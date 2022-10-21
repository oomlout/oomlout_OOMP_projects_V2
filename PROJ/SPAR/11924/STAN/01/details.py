
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11924"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11924"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Purpletooth Jamboree')
    newPart['gitRepo'].append('https://github.com/sparkfun/Purpletooth_Jamboree')
    newPart['gitName'].append('Purpletooth_Jamboree')
    newPart['eagleBoard'].append('/Hardware/Purpletooth_Jamboree.brd')
    newPart['eagleSchem'].append('/Hardware/Purpletooth_Jamboree.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

