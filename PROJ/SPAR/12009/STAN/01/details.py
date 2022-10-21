
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12009"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12009"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Logic Level Converter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Logic_Level_Converter')
    newPart['gitName'].append('Logic_Level_Converter')
    newPart['eagleBoard'].append('/Hardware/Logic_Level_Converter.brd')
    newPart['eagleSchem'].append('/Hardware/Logic_Level_Converter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

