
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13005"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13005"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TRS Jack Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/TRS_Jack_Breakout')
    newPart['gitName'].append('TRS_Jack_Breakout')
    newPart['eagleBoard'].append('/Hardware/TRS_Jack_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/TRS_Jack_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

