
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14587"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14587"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Accelerometer MMA8452Q')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Accelerometer_MMA8452Q')
    newPart['gitName'].append('Qwiic_Accelerometer_MMA8452Q')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Accelerometer-MMA8452Q.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Accelerometer-MMA8452Q.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

