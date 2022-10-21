
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14380"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14380"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adjustable Lipo Charger')
    newPart['gitRepo'].append('https://github.com/sparkfun/Adjustable_Lipo_Charger')
    newPart['gitName'].append('Adjustable_Lipo_Charger')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_Adjustable_LiPo_Charger.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_Adjustable_LiPo_Charger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

