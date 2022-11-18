
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14688"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14688"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Pressure MS5637')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Pressure-MS5637')
    newPart['gitName'].append('Qwiic_Pressure-MS5637')
    newPart['eagleBoard'].append('/Hardware/Qwiic Pressure Sensor - MS5637.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Pressure Sensor - MS5637.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

