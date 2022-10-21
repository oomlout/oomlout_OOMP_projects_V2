
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15440"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15440"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Atmospheric Sensor Breakout BME280')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Atmospheric_Sensor_Breakout_BME280')
    newPart['gitName'].append('Qwiic_Atmospheric_Sensor_Breakout_BME280')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Atmospheric_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Atmospheric_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

