
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18721"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18721"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RP2040 mikroBUS Dev Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/RP2040_mikroBUS_Dev_Board')
    newPart['gitName'].append('RP2040_mikroBUS_Dev_Board')
    newPart['eagleBoard'].append('/Hardware/RP2040_MikroBUS.brd')
    newPart['eagleSchem'].append('/Hardware/RP2040_MikroBUS.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

