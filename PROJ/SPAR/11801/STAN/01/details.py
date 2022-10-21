
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11801"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11801"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Tiny AVR Programmer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Tiny-AVR-Programmer')
    newPart['gitName'].append('Tiny-AVR-Programmer')
    newPart['eagleBoard'].append('/Hardware/Tiny_Programmer.brd')
    newPart['eagleSchem'].append('/Hardware/Tiny_Programmer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

