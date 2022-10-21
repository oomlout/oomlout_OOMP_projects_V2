
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11084"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11084"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MPL3115A2 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MPL3115A2_Breakout')
    newPart['gitName'].append('MPL3115A2_Breakout')
    newPart['eagleBoard'].append('/hardware/MPL3115A2_breakout.brd')
    newPart['eagleSchem'].append('/hardware/MPL3115A2_breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

