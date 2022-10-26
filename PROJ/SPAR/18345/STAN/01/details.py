
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18345"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Air Quality Sensor SGP40')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Air_Quality_Sensor_SGP40')
    newPart['gitName'].append('Qwiic_Air_Quality_Sensor_SGP40')
    newPart['eagleBoard'].append('/Hardware/SGP40 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SGP40 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

