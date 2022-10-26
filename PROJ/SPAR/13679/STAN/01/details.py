
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13679"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13679"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Current Sensor Breakout ACS723')
    newPart['gitRepo'].append('https://github.com/sparkfun/Current_Sensor_Breakout-ACS723')
    newPart['gitName'].append('Current_Sensor_Breakout-ACS723')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ACS723_Current_Sensor_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ACS723_Current_Sensor_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

