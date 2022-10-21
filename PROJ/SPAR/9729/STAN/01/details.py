
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9729"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9729"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ProtoScrewShield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ProtoScrewShield')
    newPart['gitName'].append('ProtoScrewShield')
    newPart['eagleBoard'].append('/Hardware/ProtoScrewShield.brd')
    newPart['eagleSchem'].append('/Hardware/ProtoScrewShield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

