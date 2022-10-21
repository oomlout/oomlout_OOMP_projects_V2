
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13034"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13034"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison I2C Breakout Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_I2C_Breakout_Block')
    newPart['gitName'].append('Edison_I2C_Breakout_Block')
    newPart['eagleBoard'].append('/Hardware/I2C_Breakout_Block.brd')
    newPart['eagleSchem'].append('/Hardware/I2C_Breakout_Block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

