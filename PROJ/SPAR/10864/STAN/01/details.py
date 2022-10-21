
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10864"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10864"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('PoEthernet Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/PoEthernet_Shield')
    newPart['gitName'].append('PoEthernet_Shield')
    newPart['eagleBoard'].append('/Hardware/PoEthernet-Shield-v11.brd')
    newPart['eagleSchem'].append('/Hardware/PoEthernet-Shield-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

