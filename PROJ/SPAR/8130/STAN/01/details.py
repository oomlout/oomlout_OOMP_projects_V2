
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8130"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8130"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('I2C Expander Breakout PCF8575')
    newPart['gitRepo'].append('https://github.com/sparkfun/I2C_Expander_Breakout-PCF8575')
    newPart['gitName'].append('I2C_Expander_Breakout-PCF8575')
    newPart['eagleBoard'].append('/Hardware/SparkFun_I2C_Expander-PCF8575.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_I2C_Expander-PCF8575.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

