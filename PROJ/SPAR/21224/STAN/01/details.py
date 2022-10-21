
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "21224"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR21224"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic MultiStar Board Promo Constellation')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_MultiStar_Board_Promo_Constellation')
    newPart['gitName'].append('Qwiic_MultiStar_Board_Promo_Constellation')
    newPart['eagleBoard'].append('/Hardware/Qwiic_MultiStar.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_MultiStar.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

