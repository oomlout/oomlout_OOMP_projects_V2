
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9825"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9825"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pocket AVR Programmer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pocket_AVR_Programmer')
    newPart['gitName'].append('Pocket_AVR_Programmer')
    newPart['eagleBoard'].append('/Hardware/AVR-Pocket-Programmer.brd')
    newPart['eagleSchem'].append('/Hardware/AVR-Pocket-Programmer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

