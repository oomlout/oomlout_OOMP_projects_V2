
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8688"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8688"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Ambient Light Sensor Breakout TEMT6000')
    newPart['gitRepo'].append('https://github.com/sparkfun/Ambient_Light_Sensor_Breakout-TEMT6000')
    newPart['gitName'].append('Ambient_Light_Sensor_Breakout-TEMT6000')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TEMT6000_Breakout-v12.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TEMT6000_Breakout-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

