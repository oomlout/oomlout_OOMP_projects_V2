
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18377"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18377"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Air Velocity Sensor FS3000 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Air_Velocity_Sensor_FS3000_Qwiic')
    newPart['gitName'].append('SparkFun_Air_Velocity_Sensor_FS3000_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_FS3000.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_FS3000.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

