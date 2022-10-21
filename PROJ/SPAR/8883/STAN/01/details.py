
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8883"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8883"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Low Current Sensor Breakout ACS712')
    newPart['gitRepo'].append('https://github.com/sparkfun/Low_Current_Sensor_Breakout-ACS712')
    newPart['gitName'].append('Low_Current_Sensor_Breakout-ACS712')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ACS712LowCurrentSensorBoard.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ACS712LowCurrentSensorBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

