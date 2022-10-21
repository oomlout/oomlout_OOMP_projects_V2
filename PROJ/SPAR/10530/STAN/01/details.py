
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10530"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10530"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Triple Axis Magnetometer HMC5883L')
    newPart['gitRepo'].append('https://github.com/sparkfun/Triple_Axis_Magnetometer-HMC5883L')
    newPart['gitName'].append('Triple_Axis_Magnetometer-HMC5883L')
    newPart['eagleBoard'].append('/Hardware/SparkFun_HMC5883L_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_HMC5883L_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

