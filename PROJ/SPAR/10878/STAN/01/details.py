
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10878"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10878"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('EL Escudo Dos')
    newPart['gitRepo'].append('https://github.com/sparkfun/EL_Escudo_Dos')
    newPart['gitName'].append('EL_Escudo_Dos')
    newPart['eagleBoard'].append('/Hardware/SparkFun_EL_Escudo_Dos.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_EL_Escudo_Dos.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

