
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19096"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19096"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Environmental Sensor BME688')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Environmental_Sensor_BME688')
    newPart['gitName'].append('Qwiic_Environmental_Sensor_BME688')
    newPart['eagleBoard'].append('/Hardware/Qwiic_BME688.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_BME688.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

