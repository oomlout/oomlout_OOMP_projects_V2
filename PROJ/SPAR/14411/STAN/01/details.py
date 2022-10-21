
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14411"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14411"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LiPo Charger Booster 5V 1A')
    newPart['gitRepo'].append('https://github.com/sparkfun/LiPo_Charger_Booster_5V_1A')
    newPart['gitName'].append('LiPo_Charger_Booster_5V_1A')
    newPart['eagleBoard'].append('/Hardware/LiPoChargerBooster5V1A.brd')
    newPart['eagleSchem'].append('/Hardware/LiPoChargerBooster5V1A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

