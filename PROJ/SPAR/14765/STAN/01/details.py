
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14765"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14765"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Single Supply Logic Level Converter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Single_Supply_Logic_Level_Converter')
    newPart['gitName'].append('Single_Supply_Logic_Level_Converter')
    newPart['eagleBoard'].append('/Hardware/Single_Supply_Logic_Level_Converter.brd')
    newPart['eagleSchem'].append('/Hardware/Single_Supply_Logic_Level_Converter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

