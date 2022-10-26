
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13944"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13944"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('9DOF Sensor Stick')
    newPart['gitRepo'].append('https://github.com/sparkfun/9DOF_Sensor_Stick')
    newPart['gitName'].append('9DOF_Sensor_Stick')
    newPart['eagleBoard'].append('/Hardware/SparkFun_9DoF_Sensor_Stick.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_9DoF_Sensor_Stick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

