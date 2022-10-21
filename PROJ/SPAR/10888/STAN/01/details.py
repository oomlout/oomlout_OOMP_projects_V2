
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10888"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10888"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LSM303 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LSM303_Breakout')
    newPart['gitName'].append('LSM303_Breakout')
    newPart['eagleBoard'].append('/Hardware/LSM303 breakout board-v12.brd')
    newPart['eagleSchem'].append('/Hardware/LSM303 breakout board-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

