
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16794"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16794"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Weather Carrier Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Weather_Carrier_Board')
    newPart['gitName'].append('MicroMod_Weather_Carrier_Board')
    newPart['eagleBoard'].append('/Hardware/MicroMod_Weather_Carrier.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_Weather_Carrier.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

