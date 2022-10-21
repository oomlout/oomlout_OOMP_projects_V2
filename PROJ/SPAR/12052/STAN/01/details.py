
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12052"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12052"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LTC4150 Coulomb Counter BOB')
    newPart['gitRepo'].append('https://github.com/sparkfun/LTC4150_Coulomb_Counter_BOB')
    newPart['gitName'].append('LTC4150_Coulomb_Counter_BOB')
    newPart['eagleBoard'].append('/Hardware/LTC4150_BOB.brd')
    newPart['eagleSchem'].append('/Hardware/LTC4150_BOB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

