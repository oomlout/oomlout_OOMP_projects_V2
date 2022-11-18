
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17072"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17072"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Multi Distance VL53L3CX')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Multi_Distance_VL53L3CX')
    newPart['gitName'].append('Qwiic_Multi_Distance_VL53L3CX')
    newPart['eagleBoard'].append('/Hardware/Qwiic Multi Distance Sensor - VL53L3CX.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Multi Distance Sensor - VL53L3CX.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

