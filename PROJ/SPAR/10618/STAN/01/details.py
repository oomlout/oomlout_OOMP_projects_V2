
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10618"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10618"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Power Driver Shield Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Power_Driver_Shield_Kit')
    newPart['gitName'].append('Power_Driver_Shield_Kit')
    newPart['eagleBoard'].append('/Hardware/PowerDriver-Shield-v13.brd')
    newPart['eagleSchem'].append('/Hardware/PowerDriver-Shield-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

