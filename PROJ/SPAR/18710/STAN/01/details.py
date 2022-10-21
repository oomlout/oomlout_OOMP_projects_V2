
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18710"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18710"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod mikroBUS Carrier Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_mikroBUS_Carrier_Board')
    newPart['gitName'].append('MicroMod_mikroBUS_Carrier_Board')
    newPart['eagleBoard'].append('/Hardware/MM_MikroBUS_Carrier.brd')
    newPart['eagleSchem'].append('/Hardware/MM_MikroBUS_Carrier.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

