
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11520"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11520"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Fio v3')
    newPart['gitRepo'].append('https://github.com/sparkfun/Fio_v3')
    newPart['gitName'].append('Fio_v3')
    newPart['eagleBoard'].append('/Hardware/Arduino-Fio.brd')
    newPart['eagleSchem'].append('/Hardware/Arduino-Fio.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

