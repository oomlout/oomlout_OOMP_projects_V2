
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LogicBlocks')
    newPart['gitRepo'].append('https://github.com/sparkfun/LogicBlocks')
    newPart['gitName'].append('LogicBlocks')
    newPart['eagleBoard'].append('/hardware/AND/logicBlocks-AND.brd')
    newPart['eagleSchem'].append('/hardware/AND/logicBlocks-AND.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

