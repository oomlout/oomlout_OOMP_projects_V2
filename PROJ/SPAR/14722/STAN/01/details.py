
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14722"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14722"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Distance VL53L1X')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Distance_VL53L1X')
    newPart['gitName'].append('Qwiic_Distance_VL53L1X')
    newPart['eagleBoard'].append('/Hardware/Qwiic Distance Sensor - VL53L1X.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Distance Sensor - VL53L1X.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

