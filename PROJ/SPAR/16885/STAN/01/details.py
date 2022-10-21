
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16885"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16885"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod ATP Carrier Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_ATP_Carrier_Board')
    newPart['gitName'].append('MicroMod_ATP_Carrier_Board')
    newPart['eagleBoard'].append('/Hardware/MicroMod_ATP_CarrierBoard.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_ATP_CarrierBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

