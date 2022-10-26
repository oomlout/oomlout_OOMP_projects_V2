
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8882"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8882"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Hall Effect Current Sensor Breakout ACS712')
    newPart['gitRepo'].append('https://github.com/sparkfun/Hall-Effect_Current_Sensor_Breakout-ACS712')
    newPart['gitName'].append('Hall-Effect_Current_Sensor_Breakout-ACS712')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ACS712_Breakout_v11.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ACS712_Breakout_v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

