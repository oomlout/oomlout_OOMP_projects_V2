
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12582"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12582"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BlueSMiRF')
    newPart['gitRepo'].append('https://github.com/sparkfun/BlueSMiRF')
    newPart['gitName'].append('BlueSMiRF')
    newPart['eagleBoard'].append('/Hardware/BlueSMiRF-ChipAnt.brd')
    newPart['eagleSchem'].append('/Hardware/BlueSMiRF-ChipAnt.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

