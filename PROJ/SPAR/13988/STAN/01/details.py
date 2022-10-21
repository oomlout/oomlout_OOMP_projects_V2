
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13988"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13988"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Micro Bit Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Micro_Bit_Breakout')
    newPart['gitName'].append('Micro_Bit_Breakout')
    newPart['eagleBoard'].append('/Hardware/Micro_Bit_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Micro_Bit_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

