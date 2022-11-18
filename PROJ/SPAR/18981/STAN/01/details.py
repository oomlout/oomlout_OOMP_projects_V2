
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18981"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18981"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Ambient Light Sensor VEML7700')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Ambient_Light_Sensor_VEML7700')
    newPart['gitName'].append('Qwiic_Ambient_Light_Sensor_VEML7700')
    newPart['eagleBoard'].append('/Hardware/Qwiic_VEML7700.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_VEML7700.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

