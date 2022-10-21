
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10182"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10182"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Monster Moto Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Monster_Moto_Shield')
    newPart['gitName'].append('Monster_Moto_Shield')
    newPart['eagleBoard'].append('/Hardware/MonsterMoto-Shield-v12.brd')
    newPart['eagleSchem'].append('/Hardware/MonsterMoto-Shield-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

