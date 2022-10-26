
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14571"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14571"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Magnetometer MLX90393')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Magnetometer_MLX90393')
    newPart['gitName'].append('Qwiic_Magnetometer_MLX90393')
    newPart['eagleBoard'].append('/Hardware/Qwiic_MLX90393_Magnetometer.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_MLX90393_Magnetometer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

