
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14001"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('9DOF Razor IMU')
    newPart['gitRepo'].append('https://github.com/sparkfun/9DOF_Razor_IMU')
    newPart['gitName'].append('9DOF_Razor_IMU')
    newPart['eagleBoard'].append('/Hardware/sparkfun-9dof-razor-imu.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun-9dof-razor-imu.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

