
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14544"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14544"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Current Sensor Breakout ACS723 Low Current')
    newPart['gitRepo'].append('https://github.com/sparkfun/Current_Sensor_Breakout-ACS723-Low_Current')
    newPart['gitName'].append('Current_Sensor_Breakout-ACS723-Low_Current')
    newPart['eagleBoard'].append('/Hardware/ACS723_Low_Current_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/ACS723_Low_Current_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

