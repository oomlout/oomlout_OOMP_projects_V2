
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11486"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11486"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MPU 9150 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MPU-9150_Breakout')
    newPart['gitName'].append('MPU-9150_Breakout')
    newPart['eagleBoard'].append('/hardware/mpu-9150_breakout.brd')
    newPart['eagleSchem'].append('/hardware/mpu-9150_breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

