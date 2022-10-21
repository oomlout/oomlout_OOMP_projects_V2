
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13339"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13339"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LSM6DS3 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LSM6DS3_Breakout')
    newPart['gitName'].append('LSM6DS3_Breakout')
    newPart['eagleBoard'].append('/Hardware/LSM6DS3_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/LSM6DS3_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

